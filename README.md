# Face Redact 🕶️

I needed a super simple way to blur faces in photos for privacy, so I made this little Python script! It's basically my first attempt at computer vision - nothing fancy, just gets the job done.

## What it does

Takes a photo, finds the faces, and blurs them out. That's it! 

I used OpenCV because my friend told me it was good for this stuff. The face detection thing is built right into it, which is pretty cool. Just point it at a photo and it automatically finds where the faces are.

## Getting it working

You need Python on your computer first. Then install the one thing it needs:

```bash
pip install opencv-python
```

That's literally it. OpenCV does everything.

## How to use it

Super easy - just give it a photo:

```bash
python face_redact.py my_photo.jpg
```

It will make a new file called `my_photo_blurred.jpg` with the faces all blurry. 

The script tells you how many faces it found, which is helpful to know if it missed anyone.

## Example

```bash
python face_redact.py family_reunion.jpg
```

Output:
```
Found 8 face(s)
Saved blurred image to: family_reunion_blurred.jpg
```

## Things I learned while making this

- Face detection works way better on clear photos where people are looking at the camera
- Sometimes it misses faces if they're turned to the side or really small
- The blur is pretty strong (I made it that way on purpose)
- It keeps the original photo and makes a new blurred one

## Why I built this

I wanted to post some group photos online but didn't want to put everyone's faces out there without asking. Photoshop seemed like overkill and I thought it would be fun to try coding something myself.

Turns out OpenCV makes this stuff way easier than I expected! The hardest part was figuring out how to save the file with a new name.

## If something breaks

The most common issues I ran into:
- Make sure the image file actually exists 
- Check that it's a normal image format (JPG, PNG, etc.)
- Sometimes really old or weird image files don't work

If you get an error, just double-check the filename and try again.

## Could be better

This is pretty basic - I know there are fancier ways to do face detection and different blur effects, but honestly this works fine for what I needed. Maybe I'll add more features later if I get motivated!

---

*Works on my machine! 🤷‍♂️*