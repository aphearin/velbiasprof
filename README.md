There are currently two csv files that I have analyzed: 

1. mdr1_fofp_0_0_0.csv (halo particles in sub-volume 000)
2. mdr1_fof.csv (all halos with Mvir > 1e13)

To run the analysis, first convert the csv files into hdf5:

$ python read_csv.py path/mdr1_fofp_0_0_0.csv
$ python read_csv.py path/mdr1_fof.csv

This will read the csv, store it into a structured numpy array, and store the result as an hdf5 file in the same path as where the csv is stored. 

Then you can simply open up the IPython Notebook and hit "Run All".