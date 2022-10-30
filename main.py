import logging
import subprocess

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

log = logging.getLogger(__name__)


class AutorandrExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        try:
            p = subprocess.check_output(["autorandr", "--detected"])
        except:
            return RenderResultListAction([
                ExtensionResultItem(icon='images/icon.png',
                                    name='Autorandr not installed',
                                    description='Please install it through your package manager',
                                    on_enter=HideWindowAction())
            ])

        # Discard the additional newline
        configs = p.decode().split('\n')[:-1]

        if not configs:
            return RenderResultListAction([
                ExtensionResultItem(icon='images/icon.png',
                                    name='Could not find any configurations',
                                    description='Autorandr did not find any configurations to switch to',
                                    on_enter=HideWindowAction())
            ])

        items = []

        # the part after the keyword
        input = event.get_argument()

        for conf in configs:
            if not input or input in conf:
                items.append(ExtensionResultItem(icon='images/icon.png',
                                                 name=f'Configuration: {conf}',
                                                 description='Item description',
                                                 on_enter=ExtensionCustomAction(conf)))

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        config = event.get_data()
        log.debug(f'applying config {config}')

        subprocess.call(["autorandr", config])


if __name__ == '__main__':
    AutorandrExtension().run()
