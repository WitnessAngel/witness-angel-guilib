import functools
import pprint
from pathlib import Path

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.config import Config
from kivy.properties import StringProperty, ListProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.textinput import TextInput
from kivymd.uix.textfield import MDTextField
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar

from waguilib.importable_settings import EXTERNAL_DATA_EXPORTS_DIR
from waguilib.logging.handlers import safe_catch_unhandled_exception

from wacryptolib.container import gather_escrow_dependencies


Builder.load_file(str(Path(__file__).parent / 'launcher_with_image_preview.kv'))



class LauncherWithImagePreviewScreen(Screen):
    pass
    """
    def __init__(self, **kwargs):
        self.title = "Witness Angel - WardProject"

        super(MainWindow, self).__init__(**kwargs)
    """
