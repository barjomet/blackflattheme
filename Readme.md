BlackFlatTheme for trac 1.2.*
=============================

Forked from https://trac-hacks.org/svn/blueflattheme/

read [COPYING.txt](COPYING.txt)

# Installation
```
pip install svn+https://trac-hacks.org/svn/themeengineplugin/trunk/
pip install git+https://github.com/barjomet/blackflattheme
```

Enable ThemeEnginePlugin and BlackFlatTheme by adding the following to your trac.ini file:

```
[components]
blueflattheme.theme.* = enabled
themeengine.* = enabled

[theme]
theme = blueflat
```

You may do this from the admin pages, too.


