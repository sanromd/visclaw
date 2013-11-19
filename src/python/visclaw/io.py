import os
import numpy as np
import pickle

class Read(object):

    def __get_vars__(self):
        r"""
        gets pickle file names and sets other enviroment variables. Based on Aron Ahmadia io petsc routines
        """

        pickle_filename = os.path.join(path, '%s.pkl' % file_prefix) + str(frame).zfill(4)
        viewer_filename = os.path.join(path, '%s.ptc' % file_prefix) + str(frame).zfill(4)
        aux_viewer_filename1 = os.path.join(path, '%s_aux.ptc' % file_prefix) + str(frame).zfill(4)
        aux_viewer_filename2 = os.path.join(path, '%s_aux.ptc' % file_prefix) + str(0).zfill(4)
        
        if os.path.exists(aux_viewer_filename1):
             aux_viewer_filename = aux_viewer_filename1
        else:
             aux_viewer_filename = aux_viewer_filename2

        if os.path.exists(pickle_filename):
            self.__setattr__('pickle_filename',pickle_filename)
            self.__setattr__('pickle_file',open(pickle_filename,'rb'))
            self.__setattr__('__pickle__',True)
        else:
            self.__setattr__('__pickle__',False)

        if os.path.exists(viewer_filename):
            self.__setattr__('viewer_filename',viewer_filename)
            self.__setattr__('__is_q__',True)
        else:
            self.__setattr__('__is_q__',False)


    def read(self):
        r"""
        Read in pickles and data from the simulation
        """
        if self.__is_q__:


    def get_patch(self):

        value_dict = pickle.load(self.pickle_file)
        for m in xrange(self.nstates):
            

    def read_pickle(self):
        r"""
        reads pickle
        """

        value_dict = pickle.load(self.pickle_file)

        # add values to viewer object in case are needed for future reference or visualization
        self.__setattr__('num_dim',value_dict['num_dim'])
        self.__setattr__('num_cells',value_dict['num_cells'])
        self.__setattr__('num_aux',value_dict['num_aux'])
        self.__setattr__('num_eqn',value_dict['num_eqn'])
        self.__setattr__('nstates',value_dict['nstates'])
    
        if self.keep_dict:
            self.__setattr__('pickle_dict'+str(frame).zfill(4),value_dict)

    def read_aux(self):
        r"""
        read only aux file
        """


    def __init__(self,frame=0,file_prefix='claw',path='./',read_aux=False,read_p=False,read_aux=False,keep_dict=False):

        self.frame       = frame
        self.file_prefix = file_prefix 
        self.path        = path
        self.read_aux    = read_aux
        self.read_aux    = read_aux
        self.read_p      = read_p
        self.keep_dict   = keep_dict
        self.read_pickle()


class Write(object):

    def split(self):
        r"""
        split q into its components and write them out
        """

    def to_vtk(self):
        r"""
        creates vtk files (ascii) from q
        """

