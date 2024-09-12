# firefox-vertical-tweaks
tweaks for tweaking firefox

### Howto

#### Install Vertical tabs
https://addons.mozilla.org/en-US/firefox/addon/tree-style-tab/

#### Adding the settings file
1. Open your active profiles root directory by searching `about:profiles` in the firefox search bar and clicking on the `Open Folder` for your root directory
2. In the chrome folder `%APPDATA%\Mozilla\Firefox\Profiles\PROFILE_NAME\chrome` create a file called `userChrome.css`
3. Copy and paste code from your OS's respective userChrome.css file in the repo into your userChrome.css file and save

#### Enabling the settings file

- Manually
1. Go to URL `about:config` 
2. Search for `toolkit.legacyUserProfileCustomizations.stylesheets` 
3. Set it to `true`
- Automatically
1. Run main.py

#### Fixing the padding
1. Press the hamburger menu and press `Customize`
2. Set the density to `Compact`

#### Finishing
Restart firefox