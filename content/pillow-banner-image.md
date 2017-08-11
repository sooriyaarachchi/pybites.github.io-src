Title: Using Pillow to Create Nice Banners For Your Site
Date: 2017-08-11 14:00
Category: Modules
Tags: Pillow, images, utilities, pybites, banners, curl, refactoring
Slug: pillow-banner-image
Authors: Bob
Summary: Running your site or business good chance you A. use promo material like banners and B. you make them manually with Photoshop, Gimp or what not. And yes for advanced one-off stuff you probably need those programs. But what if you like to keep it simple? Just an image and text on canvas? Enter [Pillow](https://python-pillow.org/) - *The friendly PIL fork*, which makes this pretty easy. Come explore some of its capabilities with me in this article.
cover: images/featured/pb-article.png

Running your site or business good chance you A. use promo material like banners and B. you make them manually with Photoshop, Gimp or what not. And yes for advanced one-off stuff you probably need those programs. But what if you like to keep it simple? Just an image and text on canvas? Enter [Pillow](https://python-pillow.org/) - *The friendly PIL fork*, which makes this pretty easy. Come explore some of its capabilities with me in this article.

> The Python Imaging Library adds image processing capabilities to your Python interpreter. - [docs](http://pillow.readthedocs.io/en/4.2.x/handbook/overview.html)

In this article we will use Pillow to create a simple promo banner for PyBites Code Challenges, starting with this week - how applicable! - [#31 - Image Manipulation With Pillow](https://pybit.es/codechallenge31.html). By the way if you like to practice this stuff yourself, you should really join this week's challenge :)

*Simple* being just 2 images on a canvas and a title using a nice font. In part 2 I will wrap a CLI and Flask app around it so you can use it providing your own inputs.

The complete code for this article is [here](https://github.com/pybites/blog_code/tree/master/pillow).

## Getting ready

First let's create a virtual env and install Pillow

	$ python3 -m venv venv && source venv/bin/activate
	(venv) $ pip install Pillow
	..
	(venv) $ pip freeze > requirements.txt
	(venv) $ mkdir banner && cd $_
	(venv) $ touch __init__.py

Let's get the images we will use for our banner.

	(venv) $ mkdir assets && cd _
	(venv) $ curl https://pybit.es/theme/img/page{-challenges.png} -o "pybites#1"
	(venv) $ curl https://pbs.twimg.com/profile_images/510760404411109380/wDGjWJxk.png -o pillow-logo.png
	(venv) $ cd ..

The `#1` tells curl to use the string I wrapped in `{}` for output filename:

## Step 1. - create a canvas and put our challenges logo on it:

Let's write some code.

_Disclaimer_: we just write it in a procedural way to get something working. We will refactor it in step 4.

Create a `banner.py` and add the following code:

	import os
	from PIL import Image, ImageDraw, ImageFont

	ASSET_DIR = 'assets'
	PB_CHALLENGE_IMG = os.path.join(ASSET_DIR, 'pybites-challenges.png')
	PILLOW_IMG = os.path.join(ASSET_DIR, 'pillow-logo.png')
	DEFAULT_WIDTH = 600
	DEFAULT_HEIGHT = 150
	DEFAULT_CANVAS_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)
	DEFAULT_TOP_MARGIN = 15
	WHITE = (255, 255, 255)

	image = Image.new('RGB', DEFAULT_CANVAS_SIZE, WHITE)

	pb_logo = Image.open(PB_CHALLENGE_IMG)
	pb_logo_offset = (0, DEFAULT_TOP_MARGIN)
	image.paste(pb_logo, pb_logo_offset)
	pb_logo_width, pb_logo_height = pb_logo.size

	image.save('out.png')

We do our imports and set up some constants. `os.path.join` is always best practice to join directories and filenames to make it compatible across different operating systems.

We create a new canvas with `Image.new` stating the dimensions and background color. We put the Pybites challenges logo at an offset of left=0, top=15. And we store the image's width use height in variables for later use.

We save the image to a file which confirms this worked:

![pillow-step1.png]({filename}/images/pillow-step1.png){.border}

## Step 2. - add a second image

The second image is the Pillow logo. But the original is 442 × 442. Let's resize it. One way is to calculate it, [like I did last time](https://github.com/pybites/100DaysOfCode/blob/master/074/text_on_image.py). Another way is using the `thumbnail` method as I found [on this SO thread](https://stackoverflow.com/questions/2232742/does-python-pil-resize-maintain-the-aspect-ratio).

The offset of this second image gets calculated so it should still work if one day I decide to change the canvas or Pybites logo image sizes.

	...

	second_img = Image.open(PILLOW_IMG)
	second_img.thumbnail(pb_logo.size, Image.ANTIALIAS)

	offset_second_img = (DEFAULT_WIDTH - pb_logo_width, DEFAULT_TOP_MARGIN)
	image.paste(second_img, offset_second_img)

	...

Resulting in:

![pillow-step2.png]({filename}/images/pillow-step2.png){.border}

Again we will clean this up later. At this stage I want to get something working, then make it reusable.

## Step 3. - add some text

Here we need the already imported `ImageDraw` and `ImageFont`.

`ImageFont.truetype` lets you work with nice fonts so let's get a [TrueType](https://en.wikipedia.org/wiki/TrueType) file. 

I used [Font Squirrel](https://www.fontsquirrel.com/) and downloaded [Ubuntu](https://www.fontsquirrel.com/fonts/list/find_fonts?q%5Bterm%5D=ubuntu&q%5Bsearch_check%5D=Y) and [Source Sans Pro](https://www.fontsquirrel.com/fonts/source-sans-pro?q%5Bterm%5D=source+sans+pro&q%5Bsearch_check%5D=Y) (latter used on PyBites). They are included in the `assets` folder.

Add this code:

	...
	BLACK = (0, 0, 0)
	TEXT_FONT_TYPE = os.path.join(ASSET_DIR, 'SourceSansPro-Regular.otf')
	TEXT_SIZE = 24
	TEXT_PADDING_HOR = 20
	TEXT_PADDING_VERT = 40
	IMG_TEXT = 'Code Challenge 31:\nImage Manipulation With Pillow'

	...

	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype(TEXT_FONT_TYPE, TEXT_SIZE)
	offset_text = (pb_logo_width + TEXT_PADDING_HOR, TEXT_PADDING_VERT)
	draw.text(offset_text, IMG_TEXT, BLACK, font=font)
	...

Again only little code needed. Final result for now:

![pillow-step3.png]({filename}/images/pillow-step3.png){.border}

## Step 4. - make it reusable

Now is a good time to commit our changes:

	(venv) $ vi .gitignore (add `out.png`)
	(venv) $ git init
	(venv) $ git add .
	(venv) $ git commit -m "first commit"

Now let's make it more reusable by turning it into a class and stuffing the constants away in `constants.py`. You can also use [`configparser`](https://docs.python.org/3/library/configparser.html) for this.

This is the final version of the script:

*constants.py*
	
	import os

	ASSET_DIR = 'assets'
	FIRST_IMAGE = os.path.join(ASSET_DIR, 'pybites-challenges.png')
	SECOND_IMAGE = os.path.join(ASSET_DIR, 'pillow-logo.png')
	DEFAULT_WIDTH = 600
	DEFAULT_HEIGHT = 150
	DEFAULT_CANVAS_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)
	DEFAULT_TOP_MARGIN = 15
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	DEFAULT_TEXT_FONT_TYPE = os.path.join(ASSET_DIR, 'SourceSansPro-Regular.otf')
	DEFAULT_TEXT_SIZE = 24
	TEXT_PADDING_HOR = 20
	TEXT_PADDING_VERT = 40
	IMG_TEXT = 'Code Challenge 31:\nImage Manipulation With Pillow'


*banner.py*

	from collections import namedtuple

	from PIL import Image, ImageDraw, ImageFont

	import constants

	Font = namedtuple('Font', 'ttf text color size offset')
	ImageDetails = namedtuple('Image', 'left top size')


	class Banner:
		def __init__(self, size=constants.DEFAULT_CANVAS_SIZE,
					 bgcolor=constants.WHITE):
			'''Creating a new canvas'''
			self.size = size
			self.bgcolor = bgcolor
			self.image = Image.new('RGB', self.size, self.bgcolor)
			self.image_coords = []

		def add_image(self, image, resize=False,
					  top=constants.DEFAULT_TOP_MARGIN, left=0, right=False):
			'''Adds (pastes) image on canvas
			If right is given calculate left, else take left
			Returns added img size'''
			img = Image.open(image)

			if resize:
				size = constants.DEFAULT_HEIGHT * 0.8
				img.thumbnail((size, size), Image.ANTIALIAS)

			if right:
				left = self.image.size[0] - img.size[0]
			else:
				left = left

			offset = (left, top)
			self.image.paste(img, offset)
			img_details = ImageDetails(left=left, top=top, size=img.size)
			self.image_coords.append(img_details)

		def add_text(self, font):
			'''Adds text on a given image object'''
			draw = ImageDraw.Draw(self.image)
			pillow_font = ImageFont.truetype(font.ttf, font.size)

			if font.offset:
				offset = font.offset
			else:
				# if no offset given put text alongside first image
				left_image_px = min(img.left + img.size[0]
									for img in self.image_coords)
				offset = (left_image_px + constants.TEXT_PADDING_HOR,
						constants.TEXT_PADDING_VERT)

			draw.text(offset, font.text, font.color, font=pillow_font)

		def save_image(self, output_file='out.png'):
			self.image.save(output_file)


	if __name__ == '__main__':
		banner = Banner()
		banner.add_image(constants.FIRST_IMAGE)
		banner.add_image(constants.SECOND_IMAGE, resize=True, right=True)

		font = Font(ttf=constants.DEFAULT_TEXT_FONT_TYPE,
					text=constants.IMG_TEXT,
					color=constants.BLACK,
					size=constants.DEFAULT_TEXT_SIZE,
					offset=None)

		banner.add_text(font)
		banner.save_image()



## What's next?

With this interface done it's time to let the user specify inputs.

I will be doing that as part of [this week's code challenge](https://pybit.es/codechallenge31.html) and follow up with a part 2 article. Ideally I provide a CLI and web (Flask) interface. Stay tuned and feel free to join our challenge and try it out yourself ...

I hope this inspires you to create your own customized banners, logos, etc. Pillow makes image manipulation easy and fun again.

---

Keep Calm and Code in Python!

-- Bob
