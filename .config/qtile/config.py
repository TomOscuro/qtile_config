from typing import List  # noqa: F401

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import subprocess
# Custom scripts
import custom_scripts.wallpapers as wpp

mod = "mod4"
terminal = guess_terminal()

### Keys ###

keys = [
    # Switch workspaces
    Key([mod],            "left"   , lazy.layout.left(),            desc="Move focus to left"),
    Key([mod],            "right"  , lazy.layout.right(),           desc="Move focus to right"),
    Key([mod],            "down"   , lazy.layout.down(),            desc="Move focus down"),
    Key([mod],            "up"     , lazy.layout.up(),              desc="Move focus up"),
    # Shuffle workspaces
    Key([mod, "shift"],   "left"   , lazy.layout.shuffle_left(),    desc="Move window to the left"),
    Key([mod, "shift"],   "right"  , lazy.layout.shuffle_right(),   desc="Move window to the right"),
    Key([mod, "shift"],   "down"   , lazy.layout.shuffle_down(),    desc="Move window down"),
    Key([mod, "shift"],   "up"     , lazy.layout.shuffle_up(),      desc="Move window up"),
    # Resize Workspaces
    Key([mod, "control"], "left"   , lazy.layout.grow_left(),       desc="Grow window to the left"),
    Key([mod, "control"], "right"  , lazy.layout.grow_right(),      desc="Grow window to the right"),
    Key([mod, "control"], "down"   , lazy.layout.grow_down(),       desc="Grow window down"),
    Key([mod, "control"], "up"     , lazy.layout.grow_up(),         desc="Grow window up"),
    Key([mod],            "n"      , lazy.layout.normalize(),       desc="Reset all window sizes"),

    Key([mod],            "q"      , lazy.window.kill(),            desc="Kill focused window"),
    Key([mod, "control"], "r"      , lazy.restart(),                desc="Restart Qtile"),
    Key([mod, "control"], "q"      , lazy.shutdown(),               desc="Shutdown Qtile"),
    Key([mod],            "r"      , lazy.spawncmd(),               desc="Spawn a command using a prompt widget"),
    Key([mod],            "Return" , lazy.spawn(terminal),          desc="Launch terminal"),
    Key([mod],            "Tab"    , lazy.spawn(terminal),          desc="Launch terminal"),
    Key([mod],            "f"      , lazy.window.toggle_floating(), desc="Toggle floating mode"),

]

pamixer_keys = [
    Key([mod, "shift"],   "i"      , lazy.spawn("pamixer -i5"),    desc="Increase volume by 10"),
    Key([mod, "shift"],   "d"      , lazy.spawn("pamixer -d5"),    desc="Decrease volume by 10"),
    Key([mod, "shift"],   "m"      , lazy.spawn("pamixer -t"),      desc="Toggle mute mode"),
]
for i in pamixer_keys:
    keys.append(i)

### Groups ###

workspaces = [
    {"name": " 1 ", "key": "1", "label": " "},
    {"name": " 2 ", "key": "2", "label": " "},
    {"name": " 3 ", "key": "3", "label": " "},
    {"name": " 4 ", "key": "4", "label": " "},
    {"name": " 5 ", "key": "5", "label": " "},
    {"name": " 6 ", "key": "6", "label": " "},
    {"name": " 7 ", "key": "7", "label": " "},
    {"name": " 8 ", "key": "8", "label": " "},
    {"name": " 9 ", "key": "9", "label": " "},
]

groups = []
for workspace in workspaces:
    groups.append(Group(name=workspace["name"], label=workspace["label"]))
    keys.append(Key([mod], workspace["key"], lazy.group[workspace["name"]].toscreen(), desc="Move view to another workspace"))
    keys.append(Key([mod, "shift"], workspace["key"], lazy.window.togroup(workspace["name"], switch_group=True), desc="Move active window to new workspace"))
###

### Layouts ###

layouts = [
    layout.Columns(
        border_normal="#3A3A3A",
        border_focus='#FFFFFF',
        border_width=3,
        margin=5,
        insert_position=1
    ),
]

widget_defaults = dict(
    #font='Kaushan Script',
    font='OpenDyslexic Nerd Font',
    fontsize=16,
    padding=3,
)
###

### Wallpaper ###
wallpapers = wpp.listWPP()
###

extension_defaults = widget_defaults.copy()

currentname = "none"

bar_text_color = "#000000"
logo_dark = '~/.config/qtile/logo/archlinux-logo-black-90dpi.png'
logo_light = '~/.config/qtile/logo/archlinux-logo-white-90dpi.png'

screens = [
    Screen(
        wallpaper=wallpapers[0],
        wallpaper_mode="fill",
        bottom=bar.Bar(
            [
                widget.Spacer(length=10),
                widget.Image(
                    filename=logo_dark, 
                    margin=0, 
                    mouse_callbacks={'Button1': lazy.spawn(f"{terminal} --hold -e neofetch")}
                ),
                widget.Spacer(),
                widget.GroupBox(
                    padding=0,
                    margin=0,
                    font='AnonymicePro Nerd Font',
                    fontsize=16,
                    use_mouse_wheel=False,
                    mouse_callbacks={"Button1":None},
                    disable_drag=True,
                    highlight_method='text',
                    this_current_screen_border="#FFFFFF",
                    inactive="#555555"
                ),
                widget.Spacer(),
                widget.Prompt(prompt="Execute: ", foreground="#FFFFFF", background="000000"),
                widget.Systray(),
                widget.Spacer(length=30),
                widget.GenPollText(
                    name = "volume",
                    fmt = "vol: {}",
                    fontsize=12,
                    foreground=bar_text_color,
                    update_interval=1,
                    func = lambda: getVol()
                ),
                #widget.Spacer(length=10),
                #widget.Battery(format='{char} {percent:2.0%}', update_interval=5, padding=30, fontsize=12, foreground=bar_text_color),
                widget.KeyboardLayout(
                    configured_keyboards=['hu', 'us'], fontsize=10, foreground=bar_text_color,
                ),
                widget.Spacer(length=10),
                widget.Clock(format='%A, %B %d %I:%M %p', foreground=bar_text_color,),
                widget.Spacer(length=10)
            ],
            20,
            margin=[ 0, 5, 2, 5 ],
            background=(0, 0, 0, 0),
        ),
    ),
]

### Other ###

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False

# Needed for some Java appscustom_scripts/__init__.py
#wmname = "LG3D"
wmname = "qtile"

# Hook for changing the group icons on the bar
@hook.subscribe.setgroup
def setActiveGroupLabel():
    for i in range(0, 9):
        qtile.groups[i].label = "󰋙 "
    qtile.current_group.label = "󰫈 "
# icon empty  "󰋙 " " " " " " "
# icon full   "󰫈 " " " " " "󰗝 " " "

### Volume Script ###

# Get volume with pamixer (used in GenPollText widget)
def getVol():
  vol = subprocess.check_output(
    ["pamixer", "--get-volume-human"]
    ).rstrip().decode("UTF-8")
  return vol
###
