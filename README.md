# hdtr-python
[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png)](http://www.wtfpl.net/)

This a python script (WIP) which renders an HDTR image from a set of pictures of the same place taken at different times (usually at intervals as if they were shot to render a timelapse). 

The aim of the project is to render an unique image in which the light flow is visible.

The HDTR concept is coined by Martin Krzywinski and is described at http://mkweb.bcgsc.ca/fun/hdtr/ who also has [a script in Perl to render the image](http://mkweb.bcgsc.ca/fun/hdtr/?code)

There is also an implementation of a [Script in Javascript that runs in Photoshop which renders a layered image](https://github.com/dgomezg/hdtr-photoshop-js)

The aim of this project is to provide an open source alternative in python that render not a final blended image but, instead, a layered tiff image.

## Sample files

Under the `samples` folder you will find some sample sets that can be used to run the script

### Source files
The repository includes some sets of low-res pictures that can be used to test the script.

### Output files
For each set of source files, there is one or more sample processed files in a final folder. You can try out your own results. The recomended output folder for your tests is `samples/**/output`. That folder is ignored by git.

## Requirements

### Pillow
This script uses Pillow, the "PIL friendly fork" that includes support for handling Tiff image files.

Pillow can be instaled through pip:

```
 sudo python3 -m pip install Pillow
```

<!--
Check that standard installation has support for tiff images, as described in
https://pillow.readthedocs.io/en/stable/installation.html#external-libraries

if not, it should probably be installed with
```
sudo python3 -m pip install pillow --global-option="build_ext" --global-option="--enable-[feature]"
```

-->

### pytest
To be able to execute the unit tests, pytest is recomended, it can be installed using:

```
python3 -m pip install -U pytest --user
```

## Try it out

To try the current status of the script, open the `hdtr_poc.py` and change the `SAMPLE_SET` to the set of initial images that you want to try out.

After that, from the project's root folder execute `python3 pocs/hdtr_poc.py`. Script will blend all the source files for the configured source `SAMPLE_SET` and the blended final image will be saved to the `output` folder of that `SAMPLE_SET`'s folder.

## See Also

- [The original HDTR site by Martin Krzywinski](http://mkweb.bcgsc.ca/fun/hdtr/)
- [An slideset explaining the shooting and rendering process](https://www.slideshare.net/dgomezg/hdtr-psjs)
