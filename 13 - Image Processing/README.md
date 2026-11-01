# Experiment 13: NumPy Image Processing

## Aim
To represent a grayscale image with a NumPy matrix and demonstrate reshaping, slicing, brightness adjustment, and matrix multiplication.

## Algorithm
1. Create 16 pixel values and reshape them into a 4×4 matrix.
2. Slice a 2×2 region from the middle.
3. Add 10 to every pixel using broadcasting and clip values to 0–255.
4. Multiply the image by a simple matrix that swaps its last two columns.

## Sample output
```text
Image matrix:
[[  0  10  20  30]
 [ 40  50  60  70]
 [ 80  90 100 110]
 [120 130 140 150]]
Selected 2x2 region:
[[ 50  60]
 [ 90 100]]
Image after increasing brightness by 10:
[[ 10  20  30  40]
 [ 50  60  70  80]
 [ 90 100 110 120]
 [130 140 150 160]]
```

## Explanation
NumPy applies `+ 10` to every pixel through broadcasting. `clip()` keeps grayscale values in range. Install NumPy if needed with `python3 -m pip install numpy`.
