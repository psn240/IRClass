# IRClass

Contributors: Rama Krishna Raju(rks395@nyu.edu) and Sudhir Nallam(psn240@nyu.edu)

# Data resizing and converting to binary format

Step 1: Upload the images to data/training-images/0 or 1 and data/test-images/0 or 1

Step 2: run: ./resize-script.sh 64 # size of the images would be converted to 64X64

Step 3: run: python convert-images-to-mnist-format.py

# Run VAE code:

Step 1 : Copy binary format data to tmp/vae/MNIST

Step 2 : run: python vae.py --working_directory tmp/vae #Runs for 64 X 64 files only.

# Run DCGAN code:

Step 1 : Copy binary format data to tmp/vae/MNIST

Step 2 : run: python gan.py --working_directory tmp/vae #Runs for 64 X 64 files only.
