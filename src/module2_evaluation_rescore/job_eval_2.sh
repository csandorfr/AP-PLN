export DRMAA_LIBRARY_PATH=/net/sge/lib/lx24-amd64/libdrmaa.so
export CGAT_HOME=/net/isi-scratch/cynthia/CGAT-DEPS
export LD_LIBRARY_PATH=$CGAT_HOME:$CGAT_HOME/Python-2.7.6_enable_shared/lib:/net/isi-scratch/cynthia/CGAT-DEPS/R-3.1.2/library:/net/isi-scratch/cynthia/CGAT-DEPS/R-3.1.2/lib:$LD_LIBRARY_PATH
export C_INCLUDE_PATH=/net/isi-scratch/cynthia/CGAT-DEPS/R-3.1.2/include
export LIBRARY_PATH=$LD_LIBRARY_PATH
source $CGAT_HOME/virtualenv-1.11.6/cgat-venv/bin/activate
export PATH=$CGAT_HOME/external-tools/bedtools2-2.19.1/bin:$CGAT_HOME/external-tools:$CGAT_HOME/external-tools/bowtie-1.1.0:$CGAT_HOME/external-tools/tophat-2.0.12.Linux_x86_64:/net/isi-scratch/src/gmap-2014-05-15/bin:/net/isi-scratch/src/subread-1.4.6-source/bin:/net/isi-scratch/src/samtools-1.2:/net/isi-scratch/cynthia/CGAT-DEPS/R-3.1.2:/net/isi-scratch/cynthia/CGAT-DEPS/R-3.1.2/bin:$PATH
export PYTHONPATH=$CGAT_HOME/cgat/CGAT:$CGAT_HOME/cgat

 cd /net/isi-scratch/cynthia/CW007_SANDOR_Pipeline/src/module2_evaluation_rescore
python pipeline_evaluation_rescore.py /net/isi-scratch/cynthia/CW007_SANDOR_Pipeline/network/all/semantic_sim_gene_all_hpo_mgi_sort.txt RNASeq_CorrelNet_pos_Excl_Less1Q95RPKM_sort /net/isi-backup/webber/code/cynthias/disease_specific_network_v4/data/frankdatasetnorm/brainspan /net/isi-scratch/cynthia/CW007_SANDOR_Pipeline/network/all 500 n
