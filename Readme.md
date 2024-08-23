# Game Template
This is project template that respect the game structure required by OLEM.

## Contents
### Code
All python files are placed here at `my_game/app`.
The entry point is always `my_game/app/main.py`.

### Assets
All assets file are to be stored in `my_game/assets`

Python functions that use assets will fetch them from this folder.

### Metadata
Contained in `my_game/metadata`, the metadata are used to used information in the menu and the mobile app.

#### Title 
The title is contained in a file at `my_game/metadata/<language_code>/title` and can be up to 64 char long (but is won't look good in OLEM's menu if it is that long).

Language code can be : 
- `fr`
- `en`

If the title does not exists or cannot be read for the current system language, the name of the root folder is displayed instead. In this case it would be `my_game`.

#### Icon 
The icon should be an 85 * 85 px image converted using https://lvgl.io/tools/imageconverter using the following parameters:
- LVGL v8
- Color format: `CF_TRUE_COLOR_ALPHA`
- Output format: `Binary RGB565`

#### Version
Does not matter during development.

## Usage
- Open the Command Center
- Connect to OLEM
- Create all directories:
  - `mkdir my_game`
  - `mkdir my_game/app`
  - `mkdir my_game/metadata`
  - `mkdir my_game/assets`
  - `mkdir my_game/assets/images`
- Load files to OLEM using the Command Center's `Upload` tab. Minimal files are:
  - All files contained in `my_game/app`
  - All files contained in `my_game/assets`
- Start the game using either the `game_start my_game` command or OLEM's on screen menu (to refresh menu, go to settings and go back to main page).
