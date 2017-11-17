### AP-PLN

### Reference

An automatic pipeline to design disease specific phenotypic linkage gene networks: AP-PLN

Viola Volpato; ;  Caleb Webber; Cynthia Sandor

### System Requirements

Running Automatic pipeline to build phenotypic linkage network (AP-PLN) requires at least Python (Python version 2.7.6) and R (R version 3.1.2). 
The following Python package must be installed: numpy (numpy version 1.9.1).
The following R packages must be installed: earth (> 4.3.3), igraph (1.1.2) and biomaRt (2.30.0). 
As no compilation is required, the pipeline can be used on any computer, where Python and R are installed and it is therefore available for Windows, Linux, and MAC OS machines. 

### AP-PLN - Download and installation

Using the buttons at the top of this page, download the ZIP file or the TAR ball, unzip/ extract the download, and save the whole AP-PLN directory (folder) in your favourite directory. The AP-PLN  directory contains directory src with source code of three modules and directories of python and R scripts. 
You need to move next in the directory AP-PLN (cd AP-PLN). 

From this URL: http://wwwfgu.anat.ox.ac.uk/downloads/compbio_projects/CW016_SANDOR_AP_PLN

You must then download and extract the following tar.gz file in your AP-PLN directory:

* [data.tar.gz](http://wwwfgu.anat.ox.ac.uk/downloads/compbio_projects/CW016_SANDOR_AP_PLN/data.tar.gz)
* [example.tar.gz](http://wwwfgu.anat.ox.ac.uk/downloads/compbio_projects/CW016_SANDOR_AP_PLN/example.tar.gz)
* [example_t2d.tar.gz](http://wwwfgu.anat.ox.ac.uk/downloads/compbio_projects/CW016_SANDOR_AP_PLN/example_t2d.tar.gz)

Finally, you must configure a environment variable, named $AP_PLN_HOME by this way: export AP_PLN_HOME=directory of AP_PLN


### Overview

AP-PLN is divided into tree modules, consisting to:

* design a specific phenotypic benchmark according to a list of mouse phenotype term selected by the user 
* evaluate and re-scale automatically genomic functional datasets on a phenotypic benchmark. 
* integrate multiple functional genomic dataset previously re-scaled on a unique phenotypic benchmark. 


### Quick Start

In your $AP_PLN_HOME/src/quick-start, you can run a python script allowing combining two functional datasets in the directory: $AP_PLN_HOME/example: coexpr_gse3594 (co-expression dataset based on the microarray transcriptional profile GSE5394) and sem_goabp by using the following command:

python run_all_pipeline.py $AP_PLN_HOME/example/semantic_sim_gene_mgi_all.scale $AP_PLN_HOME/example/list_file_data $AP_PLN_HOME /example $AP_PLN_HOME/example quick_example


You are now ready to use AP-PLN !

