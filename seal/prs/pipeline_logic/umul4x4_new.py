
import os
import sys

# dir_path = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(dir_path + '/../../')

from seal import tracem as tr

def GeneratePipeline():

	tr.rise(f=tr.NORr, i=['logic_fs__logic_fs__b_in_0.T', 'logic_fs__logic_fs__b_in_0.F'], o='logic_fs_b_in_0__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_fs__logic_fs__b_in_0.T', 'logic_fs__logic_fs__b_in_0.F'], o='logic_fs_b_in_0__done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_fs__logic_fs__b_in_1.T', 'logic_fs__logic_fs__b_in_1.F'], o='logic_fs_b_in_1__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_fs__logic_fs__b_in_1.T', 'logic_fs__logic_fs__b_in_1.F'], o='logic_fs_b_in_1__done_n', d=2.0)

	tr.rise(f=tr.Cr, i=['logic_fs_b_in_0__done_n', 'logic_fs_b_in_1__done_n'], o='logic_fs_chin_cd_n', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs_b_in_0__done_n', 'logic_fs_b_in_1__done_n'], o='logic_fs_chin_cd_n', d=3.0)

	tr.rise(f=tr.INVr, i=['logic_fs_chin_cd_n'], o='logic_fs_chin_cd', d=1.0)
	tr.fall(f=tr.INVf, i=['logic_fs_chin_cd_n'], o='logic_fs_chin_cd', d=1.0)

	tr.rise(f=tr.Cr, i=['logic_fs_chin_cd', 'logic_fs__ack_out'], o='b0__ack_in', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs_chin_cd', 'logic_fs__ack_out'], o='b0__ack_in', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ms_1__logic_ms_1__b_in_0.T', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1_b_in_0__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ms_1__logic_ms_1__b_in_0.T', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1_b_in_0__done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_ms_1__logic_ms_1__s_in_2.T', 'logic_ms_1__logic_ms_1__s_in_2.F'], o='logic_ms_1_s_in_2__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ms_1__logic_ms_1__s_in_2.T', 'logic_ms_1__logic_ms_1__s_in_2.F'], o='logic_ms_1_s_in_2__done_n', d=2.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1_s_in_2__done_n', 'logic_ms_1_b_in_0__done_n'], o='logic_ms_1_chin_cd_n', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1_s_in_2__done_n', 'logic_ms_1_b_in_0__done_n'], o='logic_ms_1_chin_cd_n', d=3.0)

	tr.rise(f=tr.INVr, i=['logic_ms_1_chin_cd_n'], o='logic_ms_1_chin_cd', d=1.0)
	tr.fall(f=tr.INVf, i=['logic_ms_1_chin_cd_n'], o='logic_ms_1_chin_cd', d=1.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1_chin_cd', 'logic_ms_1__ack_out'], o='b1__ack_in', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1_chin_cd', 'logic_ms_1__ack_out'], o='b1__ack_in', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__a_in(0).F', 'logic_ls__logic_ls__a_in(0).T'], o='logic_ls_a_in_0__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__a_in(0).F', 'logic_ls__logic_ls__a_in(0).T'], o='logic_ls_a_in_0__done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__a_in(1).F', 'logic_ls__logic_ls__a_in(1).T'], o='logic_ls_a_in_1__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__a_in(1).F', 'logic_ls__logic_ls__a_in(1).T'], o='logic_ls_a_in_1__done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__a_in(2).T', 'logic_ls__logic_ls__a_in(2).F'], o='logic_ls_a_in_2__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__a_in(2).T', 'logic_ls__logic_ls__a_in(2).F'], o='logic_ls_a_in_2__done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__a_in(3).T', 'logic_ls__logic_ls__a_in(3).F'], o='logic_ls_a_in_3__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__a_in(3).T', 'logic_ls__logic_ls__a_in(3).F'], o='logic_ls_a_in_3__done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__b_in.F'], o='logic_ls_b_in_done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__b_in.F'], o='logic_ls_b_in_done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__s_in_3.T', 'logic_ls__logic_ls__s_in_3.F'], o='logic_ls_s_in_3__done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__s_in_3.T', 'logic_ls__logic_ls__s_in_3.F'], o='logic_ls_s_in_3__done_n', d=2.0)

	tr.rise(f=tr.Cr, i=['logic_ls_a_in_0__done_n', 'logic_ls_a_in_1__done_n'], o='logic_ls_chin_cd_n_lvl0_0', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls_a_in_0__done_n', 'logic_ls_a_in_1__done_n'], o='logic_ls_chin_cd_n_lvl0_0', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls_a_in_3__done_n', 'logic_ls_a_in_2__done_n'], o='logic_ls_chin_cd_n_lvl0_1', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls_a_in_3__done_n', 'logic_ls_a_in_2__done_n'], o='logic_ls_chin_cd_n_lvl0_1', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls_b_in_done_n', 'logic_ls_s_in_3__done_n'], o='logic_ls_chin_cd_n_lvl0_2', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls_b_in_done_n', 'logic_ls_s_in_3__done_n'], o='logic_ls_chin_cd_n_lvl0_2', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls_chin_cd_n_lvl0_0', 'logic_ls_chin_cd_n_lvl0_1'], o='logic_ls_chin_cd_n_lvl1_0', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls_chin_cd_n_lvl0_0', 'logic_ls_chin_cd_n_lvl0_1'], o='logic_ls_chin_cd_n_lvl1_0', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls_chin_cd_n_lvl0_2', 'logic_ls_chin_cd_n_lvl1_0'], o='logic_ls_chin_cd_n', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls_chin_cd_n_lvl0_2', 'logic_ls_chin_cd_n_lvl1_0'], o='logic_ls_chin_cd_n', d=3.0)

	tr.rise(f=tr.INVr, i=['logic_ls_chin_cd_n'], o='logic_ls_chin_cd', d=1.0)
	tr.fall(f=tr.INVf, i=['logic_ls_chin_cd_n'], o='logic_ls_chin_cd', d=1.0)

	tr.rise(f=tr.Cr, i=['logic_ls_chin_cd', 'logic_ls__ack_out'], o='b2__ack_in', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls_chin_cd', 'logic_ls__ack_out'], o='b2__ack_in', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__done', 'logic_fs__ack_in'], o='logic_fs__ack_out', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__done', 'logic_fs__ack_in'], o='logic_fs__ack_out', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__done', 'logic_ms_1__ack_in'], o='logic_ms_1__ack_out', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__done', 'logic_ms_1__ack_in'], o='logic_ms_1__ack_out', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__ack_in', 'logic_ls__logic_ls__done'], o='logic_ls__ack_out', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__ack_in', 'logic_ls__logic_ls__done'], o='logic_ls__ack_out', d=3.0)

	tr.rise(f=tr.NORr, i=['b1__a_in(0).F', 'b1__a_in(0).T'], o='b0__c_a_out_0', d=2.0)
	tr.fall(f=tr.NORf, i=['b1__a_in(0).F', 'b1__a_in(0).T'], o='b0__c_a_out_0', d=2.0)

	tr.rise(f=tr.Cr, i=['b0__en', 'a(0).F'], o='b1__a_in(0).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__en', 'a(0).F'], o='b1__a_in(0).F', d=3.0)

	tr.rise(f=tr.Cr, i=['a(0).T', 'b0__en'], o='b1__a_in(0).T', d=3.0)
	tr.fall(f=tr.Cf, i=['a(0).T', 'b0__en'], o='b1__a_in(0).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b1__a_in(1).F', 'b1__a_in(1).T'], o='b0__c_a_out_1', d=2.0)
	tr.fall(f=tr.NORf, i=['b1__a_in(1).F', 'b1__a_in(1).T'], o='b0__c_a_out_1', d=2.0)

	tr.rise(f=tr.Cr, i=['a(1).F', 'b0__en'], o='b1__a_in(1).F', d=3.0)
	tr.fall(f=tr.Cf, i=['a(1).F', 'b0__en'], o='b1__a_in(1).F', d=3.0)

	tr.rise(f=tr.Cr, i=['a(1).T', 'b0__en'], o='b1__a_in(1).T', d=3.0)
	tr.fall(f=tr.Cf, i=['a(1).T', 'b0__en'], o='b1__a_in(1).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b1__a_in(2).F', 'b1__a_in(2).T'], o='b0__c_a_out_2', d=2.0)
	tr.fall(f=tr.NORf, i=['b1__a_in(2).F', 'b1__a_in(2).T'], o='b0__c_a_out_2', d=2.0)

	tr.rise(f=tr.Cr, i=['b0__en', 'a(2).F'], o='b1__a_in(2).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__en', 'a(2).F'], o='b1__a_in(2).F', d=3.0)

	tr.rise(f=tr.Cr, i=['a(2).T', 'b0__en'], o='b1__a_in(2).T', d=3.0)
	tr.fall(f=tr.Cf, i=['a(2).T', 'b0__en'], o='b1__a_in(2).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b1__a_in(3).T', 'b1__a_in(3).F'], o='b0__c_a_out_3', d=2.0)
	tr.fall(f=tr.NORf, i=['b1__a_in(3).T', 'b1__a_in(3).F'], o='b0__c_a_out_3', d=2.0)

	tr.rise(f=tr.Cr, i=['b0__en', 'a(3).F'], o='b1__a_in(3).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__en', 'a(3).F'], o='b1__a_in(3).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__en', 'a(3).T'], o='b1__a_in(3).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__en', 'a(3).T'], o='b1__a_in(3).T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_fs__logic_fs__b_in_0.T', 'logic_fs__logic_fs__b_in_0.F'], o='b0__c_b_out_0', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_fs__logic_fs__b_in_0.T', 'logic_fs__logic_fs__b_in_0.F'], o='b0__c_b_out_0', d=2.0)

	tr.rise(f=tr.Cr, i=['b(0).F', 'b0__en'], o='logic_fs__logic_fs__b_in_0.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b(0).F', 'b0__en'], o='logic_fs__logic_fs__b_in_0.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__en', 'b(0).T'], o='logic_fs__logic_fs__b_in_0.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__en', 'b(0).T'], o='logic_fs__logic_fs__b_in_0.T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_fs__logic_fs__b_in_1.F', 'logic_fs__logic_fs__b_in_1.T'], o='b0__c_b_out_1', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_fs__logic_fs__b_in_1.F', 'logic_fs__logic_fs__b_in_1.T'], o='b0__c_b_out_1', d=2.0)

	tr.rise(f=tr.Cr, i=['b0__en', 'b(1).F'], o='logic_fs__logic_fs__b_in_1.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__en', 'b(1).F'], o='logic_fs__logic_fs__b_in_1.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b(1).T', 'b0__en'], o='logic_fs__logic_fs__b_in_1.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b(1).T', 'b0__en'], o='logic_fs__logic_fs__b_in_1.T', d=3.0)

	tr.rise(f=tr.NORr, i=['b1__b_in(0).F', 'b1__b_in(0).T'], o='b0__c_b_out_2', d=2.0)
	tr.fall(f=tr.NORf, i=['b1__b_in(0).F', 'b1__b_in(0).T'], o='b0__c_b_out_2', d=2.0)

	tr.rise(f=tr.Cr, i=['b(2).F', 'b0__en'], o='b1__b_in(0).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b(2).F', 'b0__en'], o='b1__b_in(0).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__en', 'b(2).T'], o='b1__b_in(0).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__en', 'b(2).T'], o='b1__b_in(0).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b1__b_in(1).F', 'b1__b_in(1).T'], o='b0__c_b_out_3', d=2.0)
	tr.fall(f=tr.NORf, i=['b1__b_in(1).F', 'b1__b_in(1).T'], o='b0__c_b_out_3', d=2.0)

	tr.rise(f=tr.Cr, i=['b(3).F', 'b0__en'], o='b1__b_in(1).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b(3).F', 'b0__en'], o='b1__b_in(1).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b(3).T', 'b0__en'], o='b1__b_in(1).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b(3).T', 'b0__en'], o='b1__b_in(1).T', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__c_a_out_0', 'b0__c_a_out_1'], o='b0__ocd_n_lvl0_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__c_a_out_0', 'b0__c_a_out_1'], o='b0__ocd_n_lvl0_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__c_a_out_3', 'b0__c_a_out_2'], o='b0__ocd_n_lvl0_1', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__c_a_out_3', 'b0__c_a_out_2'], o='b0__ocd_n_lvl0_1', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__c_b_out_1', 'b0__c_b_out_0'], o='b0__ocd_n_lvl0_2', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__c_b_out_1', 'b0__c_b_out_0'], o='b0__ocd_n_lvl0_2', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__c_b_out_2', 'b0__c_b_out_3'], o='b0__ocd_n_lvl0_3', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__c_b_out_2', 'b0__c_b_out_3'], o='b0__ocd_n_lvl0_3', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__ocd_n_lvl0_0', 'b0__ocd_n_lvl0_1'], o='b0__ocd_n_lvl1_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__ocd_n_lvl0_0', 'b0__ocd_n_lvl0_1'], o='b0__ocd_n_lvl1_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__ocd_n_lvl0_3', 'b0__ocd_n_lvl0_2'], o='b0__ocd_n_lvl1_1', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__ocd_n_lvl0_3', 'b0__ocd_n_lvl0_2'], o='b0__ocd_n_lvl1_1', d=3.0)

	tr.rise(f=tr.Cr, i=['b0__ocd_n_lvl1_0', 'b0__ocd_n_lvl1_1'], o='b0__ocd_n', d=3.0)
	tr.fall(f=tr.Cf, i=['b0__ocd_n_lvl1_0', 'b0__ocd_n_lvl1_1'], o='b0__ocd_n', d=3.0)

	tr.rise(f=tr.INVr, i=['b0__ocd_n'], o='ack_out', d=1.0)
	tr.fall(f=tr.INVf, i=['b0__ocd_n'], o='ack_out', d=1.0)

	tr.rise(f=tr.INVr, i=['b0__ack_in'], o='b0__en', d=1.0)
	tr.fall(f=tr.INVf, i=['b0__ack_in'], o='b0__en', d=1.0)

	tr.rise(f=tr.NORr, i=['b2__a_in(0).F', 'b2__a_in(0).T'], o='b1__c_a_out_0', d=2.0)
	tr.fall(f=tr.NORf, i=['b2__a_in(0).F', 'b2__a_in(0).T'], o='b1__c_a_out_0', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__a_in(0).F', 'b1__en'], o='b2__a_in(0).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__a_in(0).F', 'b1__en'], o='b2__a_in(0).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__a_in(0).T', 'b1__en'], o='b2__a_in(0).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__a_in(0).T', 'b1__en'], o='b2__a_in(0).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b2__a_in(1).T', 'b2__a_in(1).F'], o='b1__c_a_out_1', d=2.0)
	tr.fall(f=tr.NORf, i=['b2__a_in(1).T', 'b2__a_in(1).F'], o='b1__c_a_out_1', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__a_in(1).F', 'b1__en'], o='b2__a_in(1).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__a_in(1).F', 'b1__en'], o='b2__a_in(1).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__a_in(1).T', 'b1__en'], o='b2__a_in(1).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__a_in(1).T', 'b1__en'], o='b2__a_in(1).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b2__a_in(2).T', 'b2__a_in(2).F'], o='b1__c_a_out_2', d=2.0)
	tr.fall(f=tr.NORf, i=['b2__a_in(2).T', 'b2__a_in(2).F'], o='b1__c_a_out_2', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__a_in(2).F', 'b1__en'], o='b2__a_in(2).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__a_in(2).F', 'b1__en'], o='b2__a_in(2).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__a_in(2).T'], o='b2__a_in(2).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__a_in(2).T'], o='b2__a_in(2).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b2__a_in(3).T', 'b2__a_in(3).F'], o='b1__c_a_out_3', d=2.0)
	tr.fall(f=tr.NORf, i=['b2__a_in(3).T', 'b2__a_in(3).F'], o='b1__c_a_out_3', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__a_in(3).F'], o='b2__a_in(3).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__a_in(3).F'], o='b2__a_in(3).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__a_in(3).T'], o='b2__a_in(3).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__a_in(3).T'], o='b2__a_in(3).T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ms_1__logic_ms_1__b_in_0.T', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='b1__c_b_out_0', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ms_1__logic_ms_1__b_in_0.T', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='b1__c_b_out_0', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__b_in(0).F', 'b1__en'], o='logic_ms_1__logic_ms_1__b_in_0.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__b_in(0).F', 'b1__en'], o='logic_ms_1__logic_ms_1__b_in_0.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__b_in(0).T'], o='logic_ms_1__logic_ms_1__b_in_0.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__b_in(0).T'], o='logic_ms_1__logic_ms_1__b_in_0.T', d=3.0)

	tr.rise(f=tr.NORr, i=['b2__b_in.F', 'b2__b_in.T'], o='b1__c_b_out_1', d=2.0)
	tr.fall(f=tr.NORf, i=['b2__b_in.F', 'b2__b_in.T'], o='b1__c_b_out_1', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__b_in(1).F', 'b1__en'], o='b2__b_in.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__b_in(1).F', 'b1__en'], o='b2__b_in.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__b_in(1).T', 'b1__en'], o='b2__b_in.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__b_in(1).T', 'b1__en'], o='b2__b_in.T', d=3.0)

	tr.rise(f=tr.NORr, i=['b2__s_in(0).T', 'b2__s_in(0).F'], o='b1__c_s_out_0', d=2.0)
	tr.fall(f=tr.NORf, i=['b2__s_in(0).T', 'b2__s_in(0).F'], o='b1__c_s_out_0', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__s_in(0).F', 'b1__en'], o='b2__s_in(0).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__s_in(0).F', 'b1__en'], o='b2__s_in(0).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__s_in(0).T', 'b1__en'], o='b2__s_in(0).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__s_in(0).T', 'b1__en'], o='b2__s_in(0).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b2__s_in(1).F', 'b2__s_in(1).T'], o='b1__c_s_out_1', d=2.0)
	tr.fall(f=tr.NORf, i=['b2__s_in(1).F', 'b2__s_in(1).T'], o='b1__c_s_out_1', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__s_in(1).F', 'b1__en'], o='b2__s_in(1).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__s_in(1).F', 'b1__en'], o='b2__s_in(1).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__s_in(1).T', 'b1__en'], o='b2__s_in(1).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__s_in(1).T', 'b1__en'], o='b2__s_in(1).T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ms_1__logic_ms_1__s_in_2.F', 'logic_ms_1__logic_ms_1__s_in_2.T'], o='b1__c_s_out_2', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ms_1__logic_ms_1__s_in_2.F', 'logic_ms_1__logic_ms_1__s_in_2.T'], o='b1__c_s_out_2', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__s_in(2).F'], o='logic_ms_1__logic_ms_1__s_in_2.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__s_in(2).F'], o='logic_ms_1__logic_ms_1__s_in_2.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__s_in(2).T'], o='logic_ms_1__logic_ms_1__s_in_2.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__s_in(2).T'], o='logic_ms_1__logic_ms_1__s_in_2.T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ms_1__logic_ms_1__s_in_3.F', 'logic_ms_1__logic_ms_1__s_in_3.T'], o='b1__c_s_out_3', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ms_1__logic_ms_1__s_in_3.F', 'logic_ms_1__logic_ms_1__s_in_3.T'], o='b1__c_s_out_3', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__s_in(3).F'], o='logic_ms_1__logic_ms_1__s_in_3.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__s_in(3).F'], o='logic_ms_1__logic_ms_1__s_in_3.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__s_in(3).T', 'b1__en'], o='logic_ms_1__logic_ms_1__s_in_3.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__s_in(3).T', 'b1__en'], o='logic_ms_1__logic_ms_1__s_in_3.T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ms_1__logic_ms_1__s_in_4.F', 'logic_ms_1__logic_ms_1__s_in_4.T'], o='b1__c_s_out_4', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ms_1__logic_ms_1__s_in_4.F', 'logic_ms_1__logic_ms_1__s_in_4.T'], o='b1__c_s_out_4', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__s_in(4).F', 'b1__en'], o='logic_ms_1__logic_ms_1__s_in_4.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__s_in(4).F', 'b1__en'], o='logic_ms_1__logic_ms_1__s_in_4.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__s_in(4).T'], o='logic_ms_1__logic_ms_1__s_in_4.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__s_in(4).T'], o='logic_ms_1__logic_ms_1__s_in_4.T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ms_1__logic_ms_1__s_in_5.T', 'logic_ms_1__logic_ms_1__s_in_5.F'], o='b1__c_s_out_5', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ms_1__logic_ms_1__s_in_5.T', 'logic_ms_1__logic_ms_1__s_in_5.F'], o='b1__c_s_out_5', d=2.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b1__s_in(5).F'], o='logic_ms_1__logic_ms_1__s_in_5.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b1__s_in(5).F'], o='logic_ms_1__logic_ms_1__s_in_5.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__s_in(5).T', 'b1__en'], o='logic_ms_1__logic_ms_1__s_in_5.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__s_in(5).T', 'b1__en'], o='logic_ms_1__logic_ms_1__s_in_5.T', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__c_a_out_0', 'b1__c_a_out_1'], o='b1__ocd_n_lvl0_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__c_a_out_0', 'b1__c_a_out_1'], o='b1__ocd_n_lvl0_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__c_a_out_3', 'b1__c_a_out_2'], o='b1__ocd_n_lvl0_1', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__c_a_out_3', 'b1__c_a_out_2'], o='b1__ocd_n_lvl0_1', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__c_b_out_1', 'b1__c_b_out_0'], o='b1__ocd_n_lvl0_2', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__c_b_out_1', 'b1__c_b_out_0'], o='b1__ocd_n_lvl0_2', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__c_s_out_0', 'b1__c_s_out_1'], o='b1__ocd_n_lvl0_3', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__c_s_out_0', 'b1__c_s_out_1'], o='b1__ocd_n_lvl0_3', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__c_s_out_3', 'b1__c_s_out_2'], o='b1__ocd_n_lvl0_4', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__c_s_out_3', 'b1__c_s_out_2'], o='b1__ocd_n_lvl0_4', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__c_s_out_5', 'b1__c_s_out_4'], o='b1__ocd_n_lvl0_5', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__c_s_out_5', 'b1__c_s_out_4'], o='b1__ocd_n_lvl0_5', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_0', 'b1__ocd_n_lvl0_1'], o='b1__ocd_n_lvl1_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_0', 'b1__ocd_n_lvl0_1'], o='b1__ocd_n_lvl1_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_2', 'b1__ocd_n_lvl0_3'], o='b1__ocd_n_lvl1_1', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_2', 'b1__ocd_n_lvl0_3'], o='b1__ocd_n_lvl1_1', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_5', 'b1__ocd_n_lvl0_4'], o='b1__ocd_n_lvl1_2', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_5', 'b1__ocd_n_lvl0_4'], o='b1__ocd_n_lvl1_2', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl1_1', 'b1__ocd_n_lvl1_0'], o='b1__ocd_n_lvl2_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl1_1', 'b1__ocd_n_lvl1_0'], o='b1__ocd_n_lvl2_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl1_2', 'b1__ocd_n_lvl2_0'], o='b1__ocd_n', d=3.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl1_2', 'b1__ocd_n_lvl2_0'], o='b1__ocd_n', d=3.0)

	tr.rise(f=tr.INVr, i=['b1__ocd_n'], o='logic_fs__ack_in', d=1.0)
	tr.fall(f=tr.INVf, i=['b1__ocd_n'], o='logic_fs__ack_in', d=1.0)

	tr.rise(f=tr.INVr, i=['b1__ack_in'], o='b1__en', d=1.0)
	tr.fall(f=tr.INVf, i=['b1__ack_in'], o='b1__en', d=1.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__a_in(0).F', 'logic_ls__logic_ls__a_in(0).T'], o='b2__c_a_out_0', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__a_in(0).F', 'logic_ls__logic_ls__a_in(0).T'], o='b2__c_a_out_0', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__a_in(0).F', 'b2__en'], o='logic_ls__logic_ls__a_in(0).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__a_in(0).F', 'b2__en'], o='logic_ls__logic_ls__a_in(0).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__a_in(0).T', 'b2__en'], o='logic_ls__logic_ls__a_in(0).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__a_in(0).T', 'b2__en'], o='logic_ls__logic_ls__a_in(0).T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__a_in(1).T', 'logic_ls__logic_ls__a_in(1).F'], o='b2__c_a_out_1', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__a_in(1).T', 'logic_ls__logic_ls__a_in(1).F'], o='b2__c_a_out_1', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__a_in(1).F'], o='logic_ls__logic_ls__a_in(1).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__a_in(1).F'], o='logic_ls__logic_ls__a_in(1).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__a_in(1).T', 'b2__en'], o='logic_ls__logic_ls__a_in(1).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__a_in(1).T', 'b2__en'], o='logic_ls__logic_ls__a_in(1).T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__a_in(2).T', 'logic_ls__logic_ls__a_in(2).F'], o='b2__c_a_out_2', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__a_in(2).T', 'logic_ls__logic_ls__a_in(2).F'], o='b2__c_a_out_2', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__a_in(2).F'], o='logic_ls__logic_ls__a_in(2).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__a_in(2).F'], o='logic_ls__logic_ls__a_in(2).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__a_in(2).T'], o='logic_ls__logic_ls__a_in(2).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__a_in(2).T'], o='logic_ls__logic_ls__a_in(2).T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__a_in(3).T', 'logic_ls__logic_ls__a_in(3).F'], o='b2__c_a_out_3', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__a_in(3).T', 'logic_ls__logic_ls__a_in(3).F'], o='b2__c_a_out_3', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__a_in(3).F'], o='logic_ls__logic_ls__a_in(3).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__a_in(3).F'], o='logic_ls__logic_ls__a_in(3).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__a_in(3).T'], o='logic_ls__logic_ls__a_in(3).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__a_in(3).T'], o='logic_ls__logic_ls__a_in(3).T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__b_in.F'], o='b2__c_b_out', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__b_in.F'], o='b2__c_b_out', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__b_in.F'], o='logic_ls__logic_ls__b_in.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__b_in.F'], o='logic_ls__logic_ls__b_in.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__b_in.T'], o='logic_ls__logic_ls__b_in.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__b_in.T'], o='logic_ls__logic_ls__b_in.T', d=3.0)

	tr.rise(f=tr.NORr, i=['b3__s_in(0).T', 'b3__s_in(0).F'], o='b2__c_s_out_0', d=2.0)
	tr.fall(f=tr.NORf, i=['b3__s_in(0).T', 'b3__s_in(0).F'], o='b2__c_s_out_0', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(0).F'], o='b3__s_in(0).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(0).F'], o='b3__s_in(0).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(0).T'], o='b3__s_in(0).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(0).T'], o='b3__s_in(0).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b3__s_in(1).T', 'b3__s_in(1).F'], o='b2__c_s_out_1', d=2.0)
	tr.fall(f=tr.NORf, i=['b3__s_in(1).T', 'b3__s_in(1).F'], o='b2__c_s_out_1', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(1).F'], o='b3__s_in(1).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(1).F'], o='b3__s_in(1).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(1).T'], o='b3__s_in(1).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(1).T'], o='b3__s_in(1).T', d=3.0)

	tr.rise(f=tr.NORr, i=['b3__s_in(2).F', 'b3__s_in(2).T'], o='b2__c_s_out_2', d=2.0)
	tr.fall(f=tr.NORf, i=['b3__s_in(2).F', 'b3__s_in(2).T'], o='b2__c_s_out_2', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(2).F'], o='b3__s_in(2).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(2).F'], o='b3__s_in(2).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(2).T'], o='b3__s_in(2).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(2).T'], o='b3__s_in(2).T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__s_in_3.T', 'logic_ls__logic_ls__s_in_3.F'], o='b2__c_s_out_3', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__s_in_3.T', 'logic_ls__logic_ls__s_in_3.F'], o='b2__c_s_out_3', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(3).F'], o='logic_ls__logic_ls__s_in_3.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(3).F'], o='logic_ls__logic_ls__s_in_3.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(3).T'], o='logic_ls__logic_ls__s_in_3.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(3).T'], o='logic_ls__logic_ls__s_in_3.T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__s_in_4.F', 'logic_ls__logic_ls__s_in_4.T'], o='b2__c_s_out_4', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__s_in_4.F', 'logic_ls__logic_ls__s_in_4.T'], o='b2__c_s_out_4', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(4).F'], o='logic_ls__logic_ls__s_in_4.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(4).F'], o='logic_ls__logic_ls__s_in_4.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(4).T'], o='logic_ls__logic_ls__s_in_4.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(4).T'], o='logic_ls__logic_ls__s_in_4.T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__s_in_5.T', 'logic_ls__logic_ls__s_in_5.F'], o='b2__c_s_out_5', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__s_in_5.T', 'logic_ls__logic_ls__s_in_5.F'], o='b2__c_s_out_5', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(5).F'], o='logic_ls__logic_ls__s_in_5.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(5).F'], o='logic_ls__logic_ls__s_in_5.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(5).T'], o='logic_ls__logic_ls__s_in_5.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(5).T'], o='logic_ls__logic_ls__s_in_5.T', d=3.0)

	tr.rise(f=tr.NORr, i=['logic_ls__logic_ls__s_in_6.F', 'logic_ls__logic_ls__s_in_6.T'], o='b2__c_s_out_6', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_ls__logic_ls__s_in_6.F', 'logic_ls__logic_ls__s_in_6.T'], o='b2__c_s_out_6', d=2.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(6).F'], o='logic_ls__logic_ls__s_in_6.F', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(6).F'], o='logic_ls__logic_ls__s_in_6.F', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__s_in(6).T'], o='logic_ls__logic_ls__s_in_6.T', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__s_in(6).T'], o='logic_ls__logic_ls__s_in_6.T', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__c_a_out_1', 'b2__c_a_out_0'], o='b2__ocd_n_lvl0_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__c_a_out_1', 'b2__c_a_out_0'], o='b2__ocd_n_lvl0_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__c_a_out_3', 'b2__c_a_out_2'], o='b2__ocd_n_lvl0_1', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__c_a_out_3', 'b2__c_a_out_2'], o='b2__ocd_n_lvl0_1', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__c_b_out', 'b2__c_s_out_0'], o='b2__ocd_n_lvl0_2', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__c_b_out', 'b2__c_s_out_0'], o='b2__ocd_n_lvl0_2', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__c_s_out_2', 'b2__c_s_out_1'], o='b2__ocd_n_lvl0_3', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__c_s_out_2', 'b2__c_s_out_1'], o='b2__ocd_n_lvl0_3', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__c_s_out_4', 'b2__c_s_out_3'], o='b2__ocd_n_lvl0_4', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__c_s_out_4', 'b2__c_s_out_3'], o='b2__ocd_n_lvl0_4', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__c_s_out_5', 'b2__c_s_out_6'], o='b2__ocd_n_lvl0_5', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__c_s_out_5', 'b2__c_s_out_6'], o='b2__ocd_n_lvl0_5', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__ocd_n_lvl0_0', 'b2__ocd_n_lvl0_1'], o='b2__ocd_n_lvl1_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__ocd_n_lvl0_0', 'b2__ocd_n_lvl0_1'], o='b2__ocd_n_lvl1_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__ocd_n_lvl0_3', 'b2__ocd_n_lvl0_2'], o='b2__ocd_n_lvl1_1', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__ocd_n_lvl0_3', 'b2__ocd_n_lvl0_2'], o='b2__ocd_n_lvl1_1', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__ocd_n_lvl0_4', 'b2__ocd_n_lvl0_5'], o='b2__ocd_n_lvl1_2', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__ocd_n_lvl0_4', 'b2__ocd_n_lvl0_5'], o='b2__ocd_n_lvl1_2', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__ocd_n_lvl1_0', 'b2__ocd_n_lvl1_1'], o='b2__ocd_n_lvl2_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__ocd_n_lvl1_0', 'b2__ocd_n_lvl1_1'], o='b2__ocd_n_lvl2_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b2__ocd_n_lvl2_0', 'b2__ocd_n_lvl1_2'], o='b2__ocd_n', d=3.0)
	tr.fall(f=tr.Cf, i=['b2__ocd_n_lvl2_0', 'b2__ocd_n_lvl1_2'], o='b2__ocd_n', d=3.0)

	tr.rise(f=tr.INVr, i=['b2__ocd_n'], o='logic_ms_1__ack_in', d=1.0)
	tr.fall(f=tr.INVf, i=['b2__ocd_n'], o='logic_ms_1__ack_in', d=1.0)

	tr.rise(f=tr.INVr, i=['b2__ack_in'], o='b2__en', d=1.0)
	tr.fall(f=tr.INVf, i=['b2__ack_in'], o='b2__en', d=1.0)

	tr.rise(f=tr.NORr, i=['s(0).F', 's(0).T'], o='b3__c_s_out_0', d=2.0)
	tr.fall(f=tr.NORf, i=['s(0).F', 's(0).T'], o='b3__c_s_out_0', d=2.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(0).F'], o='s(0).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(0).F'], o='s(0).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__s_in(0).T', 'b3__en'], o='s(0).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__s_in(0).T', 'b3__en'], o='s(0).T', d=3.0)

	tr.rise(f=tr.NORr, i=['s(1).T', 's(1).F'], o='b3__c_s_out_1', d=2.0)
	tr.fall(f=tr.NORf, i=['s(1).T', 's(1).F'], o='b3__c_s_out_1', d=2.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(1).F'], o='s(1).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(1).F'], o='s(1).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(1).T'], o='s(1).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(1).T'], o='s(1).T', d=3.0)

	tr.rise(f=tr.NORr, i=['s(2).T', 's(2).F'], o='b3__c_s_out_2', d=2.0)
	tr.fall(f=tr.NORf, i=['s(2).T', 's(2).F'], o='b3__c_s_out_2', d=2.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(2).F'], o='s(2).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(2).F'], o='s(2).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(2).T'], o='s(2).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(2).T'], o='s(2).T', d=3.0)

	tr.rise(f=tr.NORr, i=['s(3).F', 's(3).T'], o='b3__c_s_out_3', d=2.0)
	tr.fall(f=tr.NORf, i=['s(3).F', 's(3).T'], o='b3__c_s_out_3', d=2.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(3).F'], o='s(3).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(3).F'], o='s(3).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(3).T'], o='s(3).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(3).T'], o='s(3).T', d=3.0)

	tr.rise(f=tr.NORr, i=['s(4).F', 's(4).T'], o='b3__c_s_out_4', d=2.0)
	tr.fall(f=tr.NORf, i=['s(4).F', 's(4).T'], o='b3__c_s_out_4', d=2.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(4).F'], o='s(4).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(4).F'], o='s(4).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(4).T'], o='s(4).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(4).T'], o='s(4).T', d=3.0)

	tr.rise(f=tr.NORr, i=['s(5).T', 's(5).F'], o='b3__c_s_out_5', d=2.0)
	tr.fall(f=tr.NORf, i=['s(5).T', 's(5).F'], o='b3__c_s_out_5', d=2.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(5).F'], o='s(5).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(5).F'], o='s(5).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(5).T'], o='s(5).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(5).T'], o='s(5).T', d=3.0)

	tr.rise(f=tr.NORr, i=['s(6).F', 's(6).T'], o='b3__c_s_out_6', d=2.0)
	tr.fall(f=tr.NORf, i=['s(6).F', 's(6).T'], o='b3__c_s_out_6', d=2.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(6).F'], o='s(6).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(6).F'], o='s(6).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(6).T'], o='s(6).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(6).T'], o='s(6).T', d=3.0)

	tr.rise(f=tr.NORr, i=['s(7).F', 's(7).T'], o='b3__c_s_out_7', d=2.0)
	tr.fall(f=tr.NORf, i=['s(7).F', 's(7).T'], o='b3__c_s_out_7', d=2.0)

	tr.rise(f=tr.Cr, i=['b3__en', 'b3__s_in(7).F'], o='s(7).F', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__en', 'b3__s_in(7).F'], o='s(7).F', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__s_in(7).T', 'b3__en'], o='s(7).T', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__s_in(7).T', 'b3__en'], o='s(7).T', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__c_s_out_1', 'b3__c_s_out_0'], o='b3__ocd_n_lvl0_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__c_s_out_1', 'b3__c_s_out_0'], o='b3__ocd_n_lvl0_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__c_s_out_2', 'b3__c_s_out_3'], o='b3__ocd_n_lvl0_1', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__c_s_out_2', 'b3__c_s_out_3'], o='b3__ocd_n_lvl0_1', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__c_s_out_4', 'b3__c_s_out_5'], o='b3__ocd_n_lvl0_2', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__c_s_out_4', 'b3__c_s_out_5'], o='b3__ocd_n_lvl0_2', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__c_s_out_6', 'b3__c_s_out_7'], o='b3__ocd_n_lvl0_3', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__c_s_out_6', 'b3__c_s_out_7'], o='b3__ocd_n_lvl0_3', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__ocd_n_lvl0_0', 'b3__ocd_n_lvl0_1'], o='b3__ocd_n_lvl1_0', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__ocd_n_lvl0_0', 'b3__ocd_n_lvl0_1'], o='b3__ocd_n_lvl1_0', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__ocd_n_lvl0_3', 'b3__ocd_n_lvl0_2'], o='b3__ocd_n_lvl1_1', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__ocd_n_lvl0_3', 'b3__ocd_n_lvl0_2'], o='b3__ocd_n_lvl1_1', d=3.0)

	tr.rise(f=tr.Cr, i=['b3__ocd_n_lvl1_1', 'b3__ocd_n_lvl1_0'], o='b3__ocd_n', d=3.0)
	tr.fall(f=tr.Cf, i=['b3__ocd_n_lvl1_1', 'b3__ocd_n_lvl1_0'], o='b3__ocd_n', d=3.0)

	tr.rise(f=tr.INVr, i=['b3__ocd_n'], o='logic_ls__ack_in', d=1.0)
	tr.fall(f=tr.INVf, i=['b3__ocd_n'], o='logic_ls__ack_in', d=1.0)

	tr.rise(f=tr.INVr, i=['ack_in'], o='b3__en', d=1.0)
	tr.fall(f=tr.INVf, i=['ack_in'], o='b3__en', d=1.0)

	tr.rise(f=tr.NORr, i=['logic_fs__logic_fs__cell_07__b.T', 'logic_fs__logic_fs__cell_07__b.F'], o='logic_fs__logic_fs__int_sig_20_done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_fs__logic_fs__cell_07__b.T', 'logic_fs__logic_fs__cell_07__b.F'], o='logic_fs__logic_fs__int_sig_20_done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_fs__logic_fs__cell_07__a.F', 'logic_fs__logic_fs__cell_07__a.T'], o='logic_fs__logic_fs__int_sig_21_done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_fs__logic_fs__cell_07__a.F', 'logic_fs__logic_fs__cell_07__a.T'], o='logic_fs__logic_fs__int_sig_21_done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_fs__logic_fs__cell_11__a.F', 'logic_fs__logic_fs__cell_11__a.T'], o='logic_fs__logic_fs__int_sig_22_done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_fs__logic_fs__cell_11__a.F', 'logic_fs__logic_fs__cell_11__a.T'], o='logic_fs__logic_fs__int_sig_22_done_n', d=2.0)

	tr.rise(f=tr.NORr, i=['logic_fs__logic_fs__cell_11__b.T', 'logic_fs__logic_fs__cell_11__b.F'], o='logic_fs__logic_fs__int_sig_23_done_n', d=2.0)
	tr.fall(f=tr.NORf, i=['logic_fs__logic_fs__cell_11__b.T', 'logic_fs__logic_fs__cell_11__b.F'], o='logic_fs__logic_fs__int_sig_23_done_n', d=2.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__int_sig_20_done_n', 'logic_fs__logic_fs__int_sig_21_done_n'], o='logic_fs__logic_fs__internal_done_n_merged_lvl0_0', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__int_sig_20_done_n', 'logic_fs__logic_fs__int_sig_21_done_n'], o='logic_fs__logic_fs__internal_done_n_merged_lvl0_0', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__int_sig_23_done_n', 'logic_fs__logic_fs__int_sig_22_done_n'], o='logic_fs__logic_fs__internal_done_n_merged_lvl0_1', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__int_sig_23_done_n', 'logic_fs__logic_fs__int_sig_22_done_n'], o='logic_fs__logic_fs__internal_done_n_merged_lvl0_1', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__internal_done_n_merged_lvl0_0', 'logic_fs__logic_fs__internal_done_n_merged_lvl0_1'], o='logic_fs__logic_fs__internal_done_n_merged', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__internal_done_n_merged_lvl0_0', 'logic_fs__logic_fs__internal_done_n_merged_lvl0_1'], o='logic_fs__logic_fs__internal_done_n_merged', d=3.0)

	tr.rise(f=tr.INVr, i=['logic_fs__logic_fs__internal_done_n_merged'], o='logic_fs__logic_fs__done', d=1.0)
	tr.fall(f=tr.INVf, i=['logic_fs__logic_fs__internal_done_n_merged'], o='logic_fs__logic_fs__done', d=1.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__b_in_1.T', 'b1__a_in(1).T'], o='logic_fs__logic_fs__cell_12__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__b_in_1.T', 'b1__a_in(1).T'], o='logic_fs__logic_fs__cell_12__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__b_in_1.F', 'b1__a_in(1).F'], o='logic_fs__logic_fs__cell_12__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__b_in_1.F', 'b1__a_in(1).F'], o='logic_fs__logic_fs__cell_12__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__b_in_1.T', 'b1__a_in(2).T'], o='logic_fs__logic_fs__cell_13__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__b_in_1.T', 'b1__a_in(2).T'], o='logic_fs__logic_fs__cell_13__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b1__a_in(2).F', 'logic_fs__logic_fs__b_in_1.F'], o='logic_fs__logic_fs__cell_13__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b1__a_in(2).F', 'logic_fs__logic_fs__b_in_1.F'], o='logic_fs__logic_fs__cell_13__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['b1__a_in(0).T', 'logic_fs__logic_fs__b_in_0.T'], o='b1__s_in(0).T', d=3.0)
	tr.fall(f=tr.ANDf, i=['b1__a_in(0).T', 'logic_fs__logic_fs__b_in_0.T'], o='b1__s_in(0).T', d=3.0)

	tr.rise(f=tr.ORr, i=['b1__a_in(0).F', 'logic_fs__logic_fs__b_in_0.F'], o='b1__s_in(0).F', d=3.0)
	tr.fall(f=tr.ORf, i=['b1__a_in(0).F', 'logic_fs__logic_fs__b_in_0.F'], o='b1__s_in(0).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__b_in_0.T', 'b1__a_in(2).T'], o='logic_fs__logic_fs__cell_12__a.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__b_in_0.T', 'b1__a_in(2).T'], o='logic_fs__logic_fs__cell_12__a.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b1__a_in(2).F', 'logic_fs__logic_fs__b_in_0.F'], o='logic_fs__logic_fs__cell_12__a.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b1__a_in(2).F', 'logic_fs__logic_fs__b_in_0.F'], o='logic_fs__logic_fs__cell_12__a.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__b_in_0.T', 'b1__a_in(3).T'], o='logic_fs__logic_fs__cell_13__a.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__b_in_0.T', 'b1__a_in(3).T'], o='logic_fs__logic_fs__cell_13__a.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b1__a_in(3).F', 'logic_fs__logic_fs__b_in_0.F'], o='logic_fs__logic_fs__cell_13__a.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b1__a_in(3).F', 'logic_fs__logic_fs__b_in_0.F'], o='logic_fs__logic_fs__cell_13__a.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__b_in_1.T', 'b1__a_in(3).T'], o='logic_fs__logic_fs__cell_07__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__b_in_1.T', 'b1__a_in(3).T'], o='logic_fs__logic_fs__cell_07__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__b_in_1.F', 'b1__a_in(3).F'], o='logic_fs__logic_fs__cell_07__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__b_in_1.F', 'b1__a_in(3).F'], o='logic_fs__logic_fs__cell_07__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__cell_07__b.T', 'logic_fs__logic_fs__cell_07__a.T'], o='b1__s_in(5).T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__cell_07__b.T', 'logic_fs__logic_fs__cell_07__a.T'], o='b1__s_in(5).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_07__b.F', 'logic_fs__logic_fs__cell_07__a.F'], o='b1__s_in(5).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_07__b.F', 'logic_fs__logic_fs__cell_07__a.F'], o='b1__s_in(5).F', d=3.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_07__b.T', 'logic_fs__logic_fs__cell_07__a.F'], o='logic_fs__logic_fs__cell_07__nandFT', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_07__b.T', 'logic_fs__logic_fs__cell_07__a.F'], o='logic_fs__logic_fs__cell_07__nandFT', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_07__b.F', 'logic_fs__logic_fs__cell_07__a.T'], o='logic_fs__logic_fs__cell_07__nandTF', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_07__b.F', 'logic_fs__logic_fs__cell_07__a.T'], o='logic_fs__logic_fs__cell_07__nandTF', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_07__nandFT', 'logic_fs__logic_fs__cell_07__nandTF'], o='b1__s_in(4).T', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_07__nandFT', 'logic_fs__logic_fs__cell_07__nandTF'], o='b1__s_in(4).T', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_07__b.T', 'logic_fs__logic_fs__cell_07__a.T'], o='logic_fs__logic_fs__cell_07__nandTT', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_07__b.T', 'logic_fs__logic_fs__cell_07__a.T'], o='logic_fs__logic_fs__cell_07__nandTT', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_07__b.F', 'logic_fs__logic_fs__cell_07__a.F'], o='logic_fs__logic_fs__cell_07__nandFF', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_07__b.F', 'logic_fs__logic_fs__cell_07__a.F'], o='logic_fs__logic_fs__cell_07__nandFF', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_07__nandTT', 'logic_fs__logic_fs__cell_07__nandFF'], o='b1__s_in(4).F', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_07__nandTT', 'logic_fs__logic_fs__cell_07__nandFF'], o='b1__s_in(4).F', d=2.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__b_in_1.T', 'b1__a_in(0).T'], o='logic_fs__logic_fs__cell_11__a.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__b_in_1.T', 'b1__a_in(0).T'], o='logic_fs__logic_fs__cell_11__a.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b1__a_in(0).F', 'logic_fs__logic_fs__b_in_1.F'], o='logic_fs__logic_fs__cell_11__a.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b1__a_in(0).F', 'logic_fs__logic_fs__b_in_1.F'], o='logic_fs__logic_fs__cell_11__a.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['b1__a_in(1).T', 'logic_fs__logic_fs__b_in_0.T'], o='logic_fs__logic_fs__cell_11__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['b1__a_in(1).T', 'logic_fs__logic_fs__b_in_0.T'], o='logic_fs__logic_fs__cell_11__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b1__a_in(1).F', 'logic_fs__logic_fs__b_in_0.F'], o='logic_fs__logic_fs__cell_11__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b1__a_in(1).F', 'logic_fs__logic_fs__b_in_0.F'], o='logic_fs__logic_fs__cell_11__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__cell_11__b.T', 'logic_fs__logic_fs__cell_11__a.T'], o='logic_fs__logic_fs__cell_12__c_in.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__cell_11__b.T', 'logic_fs__logic_fs__cell_11__a.T'], o='logic_fs__logic_fs__cell_12__c_in.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_11__a.F', 'logic_fs__logic_fs__cell_11__b.F'], o='logic_fs__logic_fs__cell_12__c_in.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_11__a.F', 'logic_fs__logic_fs__cell_11__b.F'], o='logic_fs__logic_fs__cell_12__c_in.F', d=3.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_11__b.T', 'logic_fs__logic_fs__cell_11__a.F'], o='logic_fs__logic_fs__cell_11__nandFT', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_11__b.T', 'logic_fs__logic_fs__cell_11__a.F'], o='logic_fs__logic_fs__cell_11__nandFT', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_11__a.T', 'logic_fs__logic_fs__cell_11__b.F'], o='logic_fs__logic_fs__cell_11__nandTF', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_11__a.T', 'logic_fs__logic_fs__cell_11__b.F'], o='logic_fs__logic_fs__cell_11__nandTF', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_11__nandTF', 'logic_fs__logic_fs__cell_11__nandFT'], o='b1__s_in(1).T', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_11__nandTF', 'logic_fs__logic_fs__cell_11__nandFT'], o='b1__s_in(1).T', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_11__b.T', 'logic_fs__logic_fs__cell_11__a.T'], o='logic_fs__logic_fs__cell_11__nandTT', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_11__b.T', 'logic_fs__logic_fs__cell_11__a.T'], o='logic_fs__logic_fs__cell_11__nandTT', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_11__a.F', 'logic_fs__logic_fs__cell_11__b.F'], o='logic_fs__logic_fs__cell_11__nandFF', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_11__a.F', 'logic_fs__logic_fs__cell_11__b.F'], o='logic_fs__logic_fs__cell_11__nandFF', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_fs__logic_fs__cell_11__nandFF', 'logic_fs__logic_fs__cell_11__nandTT'], o='b1__s_in(1).F', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_fs__logic_fs__cell_11__nandFF', 'logic_fs__logic_fs__cell_11__nandTT'], o='b1__s_in(1).F', d=2.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__a.F', 'logic_fs__logic_fs__cell_12__b.F'], o='logic_fs__logic_fs__cell_12__aFbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__a.F', 'logic_fs__logic_fs__cell_12__b.F'], o='logic_fs__logic_fs__cell_12__aFbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__a.F', 'logic_fs__logic_fs__cell_12__b.T'], o='logic_fs__logic_fs__cell_12__aFbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__a.F', 'logic_fs__logic_fs__cell_12__b.T'], o='logic_fs__logic_fs__cell_12__aFbT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__b.F', 'logic_fs__logic_fs__cell_12__a.T'], o='logic_fs__logic_fs__cell_12__aTbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__b.F', 'logic_fs__logic_fs__cell_12__a.T'], o='logic_fs__logic_fs__cell_12__aTbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__a.T', 'logic_fs__logic_fs__cell_12__b.T'], o='logic_fs__logic_fs__cell_12__aTbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__a.T', 'logic_fs__logic_fs__cell_12__b.T'], o='logic_fs__logic_fs__cell_12__aTbT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_12__aTbT', 'logic_fs__logic_fs__cell_12__aFbF'], o='logic_fs__logic_fs__cell_12__x.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_12__aTbT', 'logic_fs__logic_fs__cell_12__aFbF'], o='logic_fs__logic_fs__cell_12__x.F', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_12__aTbF', 'logic_fs__logic_fs__cell_12__aFbT'], o='logic_fs__logic_fs__cell_12__x.T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_12__aTbF', 'logic_fs__logic_fs__cell_12__aFbT'], o='logic_fs__logic_fs__cell_12__x.T', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__cell_12__a.T', 'logic_fs__logic_fs__cell_12__b.T'], o='logic_fs__logic_fs__cell_12__y.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__cell_12__a.T', 'logic_fs__logic_fs__cell_12__b.T'], o='logic_fs__logic_fs__cell_12__y.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_12__a.F', 'logic_fs__logic_fs__cell_12__b.F'], o='logic_fs__logic_fs__cell_12__y.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_12__a.F', 'logic_fs__logic_fs__cell_12__b.F'], o='logic_fs__logic_fs__cell_12__y.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__c_in.F', 'logic_fs__logic_fs__cell_12__x.F'], o='logic_fs__logic_fs__cell_12__xFcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__c_in.F', 'logic_fs__logic_fs__cell_12__x.F'], o='logic_fs__logic_fs__cell_12__xFcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__c_in.T', 'logic_fs__logic_fs__cell_12__x.F'], o='logic_fs__logic_fs__cell_12__xFcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__c_in.T', 'logic_fs__logic_fs__cell_12__x.F'], o='logic_fs__logic_fs__cell_12__xFcT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__x.T', 'logic_fs__logic_fs__cell_12__c_in.F'], o='logic_fs__logic_fs__cell_12__xTcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__x.T', 'logic_fs__logic_fs__cell_12__c_in.F'], o='logic_fs__logic_fs__cell_12__xTcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__x.T', 'logic_fs__logic_fs__cell_12__c_in.T'], o='logic_fs__logic_fs__cell_12__xTcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__x.T', 'logic_fs__logic_fs__cell_12__c_in.T'], o='logic_fs__logic_fs__cell_12__xTcT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_12__xFcT', 'logic_fs__logic_fs__cell_12__xTcF'], o='b1__s_in(2).T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_12__xFcT', 'logic_fs__logic_fs__cell_12__xTcF'], o='b1__s_in(2).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_12__xFcF', 'logic_fs__logic_fs__cell_12__xTcT'], o='b1__s_in(2).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_12__xFcF', 'logic_fs__logic_fs__cell_12__xTcT'], o='b1__s_in(2).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__cell_12__x.T', 'logic_fs__logic_fs__cell_12__c_in.T'], o='logic_fs__logic_fs__cell_12__z.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__cell_12__x.T', 'logic_fs__logic_fs__cell_12__c_in.T'], o='logic_fs__logic_fs__cell_12__z.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_12__c_in.F', 'logic_fs__logic_fs__cell_12__x.F'], o='logic_fs__logic_fs__cell_12__z.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_12__c_in.F', 'logic_fs__logic_fs__cell_12__x.F'], o='logic_fs__logic_fs__cell_12__z.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__y.F', 'logic_fs__logic_fs__cell_12__z.F'], o='logic_fs__logic_fs__cell_13__c_in.F', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__y.F', 'logic_fs__logic_fs__cell_12__z.F'], o='logic_fs__logic_fs__cell_13__c_in.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__y.F', 'logic_fs__logic_fs__cell_12__z.T'], o='logic_fs__logic_fs__cell_12__yFzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__y.F', 'logic_fs__logic_fs__cell_12__z.T'], o='logic_fs__logic_fs__cell_12__yFzT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__z.F', 'logic_fs__logic_fs__cell_12__y.T'], o='logic_fs__logic_fs__cell_12__yTzF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__z.F', 'logic_fs__logic_fs__cell_12__y.T'], o='logic_fs__logic_fs__cell_12__yTzF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_12__z.T', 'logic_fs__logic_fs__cell_12__y.T'], o='logic_fs__logic_fs__cell_12__yTzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_12__z.T', 'logic_fs__logic_fs__cell_12__y.T'], o='logic_fs__logic_fs__cell_12__yTzT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_12__yTzF', 'logic_fs__logic_fs__cell_12__yFzT', 'logic_fs__logic_fs__cell_12__yTzT'], o='logic_fs__logic_fs__cell_13__c_in.T', d=3.5)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_12__yTzF', 'logic_fs__logic_fs__cell_12__yFzT', 'logic_fs__logic_fs__cell_12__yTzT'], o='logic_fs__logic_fs__cell_13__c_in.T', d=3.5)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__b.F', 'logic_fs__logic_fs__cell_13__a.F'], o='logic_fs__logic_fs__cell_13__aFbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__b.F', 'logic_fs__logic_fs__cell_13__a.F'], o='logic_fs__logic_fs__cell_13__aFbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__a.F', 'logic_fs__logic_fs__cell_13__b.T'], o='logic_fs__logic_fs__cell_13__aFbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__a.F', 'logic_fs__logic_fs__cell_13__b.T'], o='logic_fs__logic_fs__cell_13__aFbT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__b.F', 'logic_fs__logic_fs__cell_13__a.T'], o='logic_fs__logic_fs__cell_13__aTbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__b.F', 'logic_fs__logic_fs__cell_13__a.T'], o='logic_fs__logic_fs__cell_13__aTbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__a.T', 'logic_fs__logic_fs__cell_13__b.T'], o='logic_fs__logic_fs__cell_13__aTbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__a.T', 'logic_fs__logic_fs__cell_13__b.T'], o='logic_fs__logic_fs__cell_13__aTbT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_13__aFbF', 'logic_fs__logic_fs__cell_13__aTbT'], o='logic_fs__logic_fs__cell_13__x.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_13__aFbF', 'logic_fs__logic_fs__cell_13__aTbT'], o='logic_fs__logic_fs__cell_13__x.F', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_13__aFbT', 'logic_fs__logic_fs__cell_13__aTbF'], o='logic_fs__logic_fs__cell_13__x.T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_13__aFbT', 'logic_fs__logic_fs__cell_13__aTbF'], o='logic_fs__logic_fs__cell_13__x.T', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__cell_13__a.T', 'logic_fs__logic_fs__cell_13__b.T'], o='logic_fs__logic_fs__cell_13__y.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__cell_13__a.T', 'logic_fs__logic_fs__cell_13__b.T'], o='logic_fs__logic_fs__cell_13__y.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_13__b.F', 'logic_fs__logic_fs__cell_13__a.F'], o='logic_fs__logic_fs__cell_13__y.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_13__b.F', 'logic_fs__logic_fs__cell_13__a.F'], o='logic_fs__logic_fs__cell_13__y.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__x.F', 'logic_fs__logic_fs__cell_13__c_in.F'], o='logic_fs__logic_fs__cell_13__xFcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__x.F', 'logic_fs__logic_fs__cell_13__c_in.F'], o='logic_fs__logic_fs__cell_13__xFcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__x.F', 'logic_fs__logic_fs__cell_13__c_in.T'], o='logic_fs__logic_fs__cell_13__xFcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__x.F', 'logic_fs__logic_fs__cell_13__c_in.T'], o='logic_fs__logic_fs__cell_13__xFcT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__c_in.F', 'logic_fs__logic_fs__cell_13__x.T'], o='logic_fs__logic_fs__cell_13__xTcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__c_in.F', 'logic_fs__logic_fs__cell_13__x.T'], o='logic_fs__logic_fs__cell_13__xTcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__c_in.T', 'logic_fs__logic_fs__cell_13__x.T'], o='logic_fs__logic_fs__cell_13__xTcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__c_in.T', 'logic_fs__logic_fs__cell_13__x.T'], o='logic_fs__logic_fs__cell_13__xTcT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_13__xTcF', 'logic_fs__logic_fs__cell_13__xFcT'], o='b1__s_in(3).T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_13__xTcF', 'logic_fs__logic_fs__cell_13__xFcT'], o='b1__s_in(3).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_13__xTcT', 'logic_fs__logic_fs__cell_13__xFcF'], o='b1__s_in(3).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_13__xTcT', 'logic_fs__logic_fs__cell_13__xFcF'], o='b1__s_in(3).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_fs__logic_fs__cell_13__c_in.T', 'logic_fs__logic_fs__cell_13__x.T'], o='logic_fs__logic_fs__cell_13__z.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_fs__logic_fs__cell_13__c_in.T', 'logic_fs__logic_fs__cell_13__x.T'], o='logic_fs__logic_fs__cell_13__z.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_13__x.F', 'logic_fs__logic_fs__cell_13__c_in.F'], o='logic_fs__logic_fs__cell_13__z.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_13__x.F', 'logic_fs__logic_fs__cell_13__c_in.F'], o='logic_fs__logic_fs__cell_13__z.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__z.F', 'logic_fs__logic_fs__cell_13__y.F'], o='logic_fs__logic_fs__cell_07__a.F', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__z.F', 'logic_fs__logic_fs__cell_13__y.F'], o='logic_fs__logic_fs__cell_07__a.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__z.T', 'logic_fs__logic_fs__cell_13__y.F'], o='logic_fs__logic_fs__cell_13__yFzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__z.T', 'logic_fs__logic_fs__cell_13__y.F'], o='logic_fs__logic_fs__cell_13__yFzT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__z.F', 'logic_fs__logic_fs__cell_13__y.T'], o='logic_fs__logic_fs__cell_13__yTzF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__z.F', 'logic_fs__logic_fs__cell_13__y.T'], o='logic_fs__logic_fs__cell_13__yTzF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_fs__logic_fs__cell_13__z.T', 'logic_fs__logic_fs__cell_13__y.T'], o='logic_fs__logic_fs__cell_13__yTzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_fs__logic_fs__cell_13__z.T', 'logic_fs__logic_fs__cell_13__y.T'], o='logic_fs__logic_fs__cell_13__yTzT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_fs__logic_fs__cell_13__yTzT', 'logic_fs__logic_fs__cell_13__yFzT', 'logic_fs__logic_fs__cell_13__yTzF'], o='logic_fs__logic_fs__cell_07__a.T', d=3.5)
	tr.fall(f=tr.ORf, i=['logic_fs__logic_fs__cell_13__yTzT', 'logic_fs__logic_fs__cell_13__yFzT', 'logic_fs__logic_fs__cell_13__yTzF'], o='logic_fs__logic_fs__cell_07__a.T', d=3.5)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_5__b.T', 'logic_ms_1__logic_ms_1__cell_5__b.F'], o='logic_ms_1__logic_ms_1__done', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_5__b.T', 'logic_ms_1__logic_ms_1__cell_5__b.F'], o='logic_ms_1__logic_ms_1__done', d=3.0)

	tr.rise(f=tr.ANDr, i=['b2__a_in(1).T', 'logic_ms_1__logic_ms_1__b_in_0.T'], o='logic_ms_1__logic_ms_1__cell_6__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['b2__a_in(1).T', 'logic_ms_1__logic_ms_1__b_in_0.T'], o='logic_ms_1__logic_ms_1__cell_6__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b2__a_in(1).F', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1__logic_ms_1__cell_6__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b2__a_in(1).F', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1__logic_ms_1__cell_6__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['b2__a_in(2).T', 'logic_ms_1__logic_ms_1__b_in_0.T'], o='logic_ms_1__logic_ms_1__cell_7__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['b2__a_in(2).T', 'logic_ms_1__logic_ms_1__b_in_0.T'], o='logic_ms_1__logic_ms_1__cell_7__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b2__a_in(2).F', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1__logic_ms_1__cell_7__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b2__a_in(2).F', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1__logic_ms_1__cell_7__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['b2__a_in(3).T', 'logic_ms_1__logic_ms_1__b_in_0.T'], o='logic_ms_1__logic_ms_1__cell_8__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['b2__a_in(3).T', 'logic_ms_1__logic_ms_1__b_in_0.T'], o='logic_ms_1__logic_ms_1__cell_8__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b2__a_in(3).F', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1__logic_ms_1__cell_8__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b2__a_in(3).F', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1__logic_ms_1__cell_8__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['b2__a_in(0).T', 'logic_ms_1__logic_ms_1__b_in_0.T'], o='logic_ms_1__logic_ms_1__cell_5__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['b2__a_in(0).T', 'logic_ms_1__logic_ms_1__b_in_0.T'], o='logic_ms_1__logic_ms_1__cell_5__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['b2__a_in(0).F', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1__logic_ms_1__cell_5__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['b2__a_in(0).F', 'logic_ms_1__logic_ms_1__b_in_0.F'], o='logic_ms_1__logic_ms_1__cell_5__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ms_1__logic_ms_1__s_in_2.T', 'logic_ms_1__logic_ms_1__cell_5__b.T'], o='logic_ms_1__logic_ms_1__cell_6__c_in.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ms_1__logic_ms_1__s_in_2.T', 'logic_ms_1__logic_ms_1__cell_5__b.T'], o='logic_ms_1__logic_ms_1__cell_6__c_in.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__s_in_2.F', 'logic_ms_1__logic_ms_1__cell_5__b.F'], o='logic_ms_1__logic_ms_1__cell_6__c_in.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__s_in_2.F', 'logic_ms_1__logic_ms_1__cell_5__b.F'], o='logic_ms_1__logic_ms_1__cell_6__c_in.F', d=3.0)

	tr.rise(f=tr.NANDr, i=['logic_ms_1__logic_ms_1__s_in_2.F', 'logic_ms_1__logic_ms_1__cell_5__b.T'], o='logic_ms_1__logic_ms_1__cell_5__nandFT', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ms_1__logic_ms_1__s_in_2.F', 'logic_ms_1__logic_ms_1__cell_5__b.T'], o='logic_ms_1__logic_ms_1__cell_5__nandFT', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ms_1__logic_ms_1__s_in_2.T', 'logic_ms_1__logic_ms_1__cell_5__b.F'], o='logic_ms_1__logic_ms_1__cell_5__nandTF', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ms_1__logic_ms_1__s_in_2.T', 'logic_ms_1__logic_ms_1__cell_5__b.F'], o='logic_ms_1__logic_ms_1__cell_5__nandTF', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ms_1__logic_ms_1__cell_5__nandFT', 'logic_ms_1__logic_ms_1__cell_5__nandTF'], o='b2__s_in(2).T', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ms_1__logic_ms_1__cell_5__nandFT', 'logic_ms_1__logic_ms_1__cell_5__nandTF'], o='b2__s_in(2).T', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ms_1__logic_ms_1__s_in_2.T', 'logic_ms_1__logic_ms_1__cell_5__b.T'], o='logic_ms_1__logic_ms_1__cell_5__nandTT', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ms_1__logic_ms_1__s_in_2.T', 'logic_ms_1__logic_ms_1__cell_5__b.T'], o='logic_ms_1__logic_ms_1__cell_5__nandTT', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ms_1__logic_ms_1__s_in_2.F', 'logic_ms_1__logic_ms_1__cell_5__b.F'], o='logic_ms_1__logic_ms_1__cell_5__nandFF', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ms_1__logic_ms_1__s_in_2.F', 'logic_ms_1__logic_ms_1__cell_5__b.F'], o='logic_ms_1__logic_ms_1__cell_5__nandFF', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ms_1__logic_ms_1__cell_5__nandTT', 'logic_ms_1__logic_ms_1__cell_5__nandFF'], o='b2__s_in(2).F', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ms_1__logic_ms_1__cell_5__nandTT', 'logic_ms_1__logic_ms_1__cell_5__nandFF'], o='b2__s_in(2).F', d=2.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__s_in_3.F', 'logic_ms_1__logic_ms_1__cell_6__b.F'], o='logic_ms_1__logic_ms_1__cell_6__aFbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__s_in_3.F', 'logic_ms_1__logic_ms_1__cell_6__b.F'], o='logic_ms_1__logic_ms_1__cell_6__aFbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__s_in_3.F', 'logic_ms_1__logic_ms_1__cell_6__b.T'], o='logic_ms_1__logic_ms_1__cell_6__aFbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__s_in_3.F', 'logic_ms_1__logic_ms_1__cell_6__b.T'], o='logic_ms_1__logic_ms_1__cell_6__aFbT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__b.F', 'logic_ms_1__logic_ms_1__s_in_3.T'], o='logic_ms_1__logic_ms_1__cell_6__aTbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__b.F', 'logic_ms_1__logic_ms_1__s_in_3.T'], o='logic_ms_1__logic_ms_1__cell_6__aTbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__s_in_3.T', 'logic_ms_1__logic_ms_1__cell_6__b.T'], o='logic_ms_1__logic_ms_1__cell_6__aTbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__s_in_3.T', 'logic_ms_1__logic_ms_1__cell_6__b.T'], o='logic_ms_1__logic_ms_1__cell_6__aTbT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_6__aFbF', 'logic_ms_1__logic_ms_1__cell_6__aTbT'], o='logic_ms_1__logic_ms_1__cell_6__x.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_6__aFbF', 'logic_ms_1__logic_ms_1__cell_6__aTbT'], o='logic_ms_1__logic_ms_1__cell_6__x.F', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_6__aFbT', 'logic_ms_1__logic_ms_1__cell_6__aTbF'], o='logic_ms_1__logic_ms_1__cell_6__x.T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_6__aFbT', 'logic_ms_1__logic_ms_1__cell_6__aTbF'], o='logic_ms_1__logic_ms_1__cell_6__x.T', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ms_1__logic_ms_1__s_in_3.T', 'logic_ms_1__logic_ms_1__cell_6__b.T'], o='logic_ms_1__logic_ms_1__cell_6__y.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ms_1__logic_ms_1__s_in_3.T', 'logic_ms_1__logic_ms_1__cell_6__b.T'], o='logic_ms_1__logic_ms_1__cell_6__y.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__s_in_3.F', 'logic_ms_1__logic_ms_1__cell_6__b.F'], o='logic_ms_1__logic_ms_1__cell_6__y.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__s_in_3.F', 'logic_ms_1__logic_ms_1__cell_6__b.F'], o='logic_ms_1__logic_ms_1__cell_6__y.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__x.F', 'logic_ms_1__logic_ms_1__cell_6__c_in.F'], o='logic_ms_1__logic_ms_1__cell_6__xFcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__x.F', 'logic_ms_1__logic_ms_1__cell_6__c_in.F'], o='logic_ms_1__logic_ms_1__cell_6__xFcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__x.F', 'logic_ms_1__logic_ms_1__cell_6__c_in.T'], o='logic_ms_1__logic_ms_1__cell_6__xFcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__x.F', 'logic_ms_1__logic_ms_1__cell_6__c_in.T'], o='logic_ms_1__logic_ms_1__cell_6__xFcT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__x.T', 'logic_ms_1__logic_ms_1__cell_6__c_in.F'], o='logic_ms_1__logic_ms_1__cell_6__xTcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__x.T', 'logic_ms_1__logic_ms_1__cell_6__c_in.F'], o='logic_ms_1__logic_ms_1__cell_6__xTcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__x.T', 'logic_ms_1__logic_ms_1__cell_6__c_in.T'], o='logic_ms_1__logic_ms_1__cell_6__xTcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__x.T', 'logic_ms_1__logic_ms_1__cell_6__c_in.T'], o='logic_ms_1__logic_ms_1__cell_6__xTcT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_6__xFcT', 'logic_ms_1__logic_ms_1__cell_6__xTcF'], o='b2__s_in(3).T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_6__xFcT', 'logic_ms_1__logic_ms_1__cell_6__xTcF'], o='b2__s_in(3).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_6__xTcT', 'logic_ms_1__logic_ms_1__cell_6__xFcF'], o='b2__s_in(3).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_6__xTcT', 'logic_ms_1__logic_ms_1__cell_6__xFcF'], o='b2__s_in(3).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ms_1__logic_ms_1__cell_6__x.T', 'logic_ms_1__logic_ms_1__cell_6__c_in.T'], o='logic_ms_1__logic_ms_1__cell_6__z.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ms_1__logic_ms_1__cell_6__x.T', 'logic_ms_1__logic_ms_1__cell_6__c_in.T'], o='logic_ms_1__logic_ms_1__cell_6__z.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_6__x.F', 'logic_ms_1__logic_ms_1__cell_6__c_in.F'], o='logic_ms_1__logic_ms_1__cell_6__z.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_6__x.F', 'logic_ms_1__logic_ms_1__cell_6__c_in.F'], o='logic_ms_1__logic_ms_1__cell_6__z.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__z.F', 'logic_ms_1__logic_ms_1__cell_6__y.F'], o='logic_ms_1__logic_ms_1__cell_7__c_in.F', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__z.F', 'logic_ms_1__logic_ms_1__cell_6__y.F'], o='logic_ms_1__logic_ms_1__cell_7__c_in.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__z.T', 'logic_ms_1__logic_ms_1__cell_6__y.F'], o='logic_ms_1__logic_ms_1__cell_6__yFzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__z.T', 'logic_ms_1__logic_ms_1__cell_6__y.F'], o='logic_ms_1__logic_ms_1__cell_6__yFzT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__z.F', 'logic_ms_1__logic_ms_1__cell_6__y.T'], o='logic_ms_1__logic_ms_1__cell_6__yTzF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__z.F', 'logic_ms_1__logic_ms_1__cell_6__y.T'], o='logic_ms_1__logic_ms_1__cell_6__yTzF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_6__y.T', 'logic_ms_1__logic_ms_1__cell_6__z.T'], o='logic_ms_1__logic_ms_1__cell_6__yTzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_6__y.T', 'logic_ms_1__logic_ms_1__cell_6__z.T'], o='logic_ms_1__logic_ms_1__cell_6__yTzT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_6__yTzT', 'logic_ms_1__logic_ms_1__cell_6__yTzF', 'logic_ms_1__logic_ms_1__cell_6__yFzT'], o='logic_ms_1__logic_ms_1__cell_7__c_in.T', d=3.5)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_6__yTzT', 'logic_ms_1__logic_ms_1__cell_6__yTzF', 'logic_ms_1__logic_ms_1__cell_6__yFzT'], o='logic_ms_1__logic_ms_1__cell_7__c_in.T', d=3.5)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__s_in_4.F', 'logic_ms_1__logic_ms_1__cell_7__b.F'], o='logic_ms_1__logic_ms_1__cell_7__aFbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__s_in_4.F', 'logic_ms_1__logic_ms_1__cell_7__b.F'], o='logic_ms_1__logic_ms_1__cell_7__aFbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__s_in_4.F', 'logic_ms_1__logic_ms_1__cell_7__b.T'], o='logic_ms_1__logic_ms_1__cell_7__aFbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__s_in_4.F', 'logic_ms_1__logic_ms_1__cell_7__b.T'], o='logic_ms_1__logic_ms_1__cell_7__aFbT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__s_in_4.T', 'logic_ms_1__logic_ms_1__cell_7__b.F'], o='logic_ms_1__logic_ms_1__cell_7__aTbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__s_in_4.T', 'logic_ms_1__logic_ms_1__cell_7__b.F'], o='logic_ms_1__logic_ms_1__cell_7__aTbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__b.T', 'logic_ms_1__logic_ms_1__s_in_4.T'], o='logic_ms_1__logic_ms_1__cell_7__aTbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__b.T', 'logic_ms_1__logic_ms_1__s_in_4.T'], o='logic_ms_1__logic_ms_1__cell_7__aTbT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_7__aFbF', 'logic_ms_1__logic_ms_1__cell_7__aTbT'], o='logic_ms_1__logic_ms_1__cell_7__x.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_7__aFbF', 'logic_ms_1__logic_ms_1__cell_7__aTbT'], o='logic_ms_1__logic_ms_1__cell_7__x.F', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_7__aTbF', 'logic_ms_1__logic_ms_1__cell_7__aFbT'], o='logic_ms_1__logic_ms_1__cell_7__x.T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_7__aTbF', 'logic_ms_1__logic_ms_1__cell_7__aFbT'], o='logic_ms_1__logic_ms_1__cell_7__x.T', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ms_1__logic_ms_1__cell_7__b.T', 'logic_ms_1__logic_ms_1__s_in_4.T'], o='logic_ms_1__logic_ms_1__cell_7__y.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ms_1__logic_ms_1__cell_7__b.T', 'logic_ms_1__logic_ms_1__s_in_4.T'], o='logic_ms_1__logic_ms_1__cell_7__y.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__s_in_4.F', 'logic_ms_1__logic_ms_1__cell_7__b.F'], o='logic_ms_1__logic_ms_1__cell_7__y.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__s_in_4.F', 'logic_ms_1__logic_ms_1__cell_7__b.F'], o='logic_ms_1__logic_ms_1__cell_7__y.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__c_in.F', 'logic_ms_1__logic_ms_1__cell_7__x.F'], o='logic_ms_1__logic_ms_1__cell_7__xFcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__c_in.F', 'logic_ms_1__logic_ms_1__cell_7__x.F'], o='logic_ms_1__logic_ms_1__cell_7__xFcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__c_in.T', 'logic_ms_1__logic_ms_1__cell_7__x.F'], o='logic_ms_1__logic_ms_1__cell_7__xFcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__c_in.T', 'logic_ms_1__logic_ms_1__cell_7__x.F'], o='logic_ms_1__logic_ms_1__cell_7__xFcT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__x.T', 'logic_ms_1__logic_ms_1__cell_7__c_in.F'], o='logic_ms_1__logic_ms_1__cell_7__xTcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__x.T', 'logic_ms_1__logic_ms_1__cell_7__c_in.F'], o='logic_ms_1__logic_ms_1__cell_7__xTcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__x.T', 'logic_ms_1__logic_ms_1__cell_7__c_in.T'], o='logic_ms_1__logic_ms_1__cell_7__xTcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__x.T', 'logic_ms_1__logic_ms_1__cell_7__c_in.T'], o='logic_ms_1__logic_ms_1__cell_7__xTcT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_7__xFcT', 'logic_ms_1__logic_ms_1__cell_7__xTcF'], o='b2__s_in(4).T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_7__xFcT', 'logic_ms_1__logic_ms_1__cell_7__xTcF'], o='b2__s_in(4).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_7__xFcF', 'logic_ms_1__logic_ms_1__cell_7__xTcT'], o='b2__s_in(4).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_7__xFcF', 'logic_ms_1__logic_ms_1__cell_7__xTcT'], o='b2__s_in(4).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ms_1__logic_ms_1__cell_7__x.T', 'logic_ms_1__logic_ms_1__cell_7__c_in.T'], o='logic_ms_1__logic_ms_1__cell_7__z.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ms_1__logic_ms_1__cell_7__x.T', 'logic_ms_1__logic_ms_1__cell_7__c_in.T'], o='logic_ms_1__logic_ms_1__cell_7__z.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_7__c_in.F', 'logic_ms_1__logic_ms_1__cell_7__x.F'], o='logic_ms_1__logic_ms_1__cell_7__z.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_7__c_in.F', 'logic_ms_1__logic_ms_1__cell_7__x.F'], o='logic_ms_1__logic_ms_1__cell_7__z.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__y.F', 'logic_ms_1__logic_ms_1__cell_7__z.F'], o='logic_ms_1__logic_ms_1__cell_8__c_in.F', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__y.F', 'logic_ms_1__logic_ms_1__cell_7__z.F'], o='logic_ms_1__logic_ms_1__cell_8__c_in.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__z.T', 'logic_ms_1__logic_ms_1__cell_7__y.F'], o='logic_ms_1__logic_ms_1__cell_7__yFzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__z.T', 'logic_ms_1__logic_ms_1__cell_7__y.F'], o='logic_ms_1__logic_ms_1__cell_7__yFzT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__z.F', 'logic_ms_1__logic_ms_1__cell_7__y.T'], o='logic_ms_1__logic_ms_1__cell_7__yTzF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__z.F', 'logic_ms_1__logic_ms_1__cell_7__y.T'], o='logic_ms_1__logic_ms_1__cell_7__yTzF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_7__z.T', 'logic_ms_1__logic_ms_1__cell_7__y.T'], o='logic_ms_1__logic_ms_1__cell_7__yTzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_7__z.T', 'logic_ms_1__logic_ms_1__cell_7__y.T'], o='logic_ms_1__logic_ms_1__cell_7__yTzT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_7__yFzT', 'logic_ms_1__logic_ms_1__cell_7__yTzF', 'logic_ms_1__logic_ms_1__cell_7__yTzT'], o='logic_ms_1__logic_ms_1__cell_8__c_in.T', d=3.5)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_7__yFzT', 'logic_ms_1__logic_ms_1__cell_7__yTzF', 'logic_ms_1__logic_ms_1__cell_7__yTzT'], o='logic_ms_1__logic_ms_1__cell_8__c_in.T', d=3.5)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__b.F', 'logic_ms_1__logic_ms_1__s_in_5.F'], o='logic_ms_1__logic_ms_1__cell_8__aFbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__b.F', 'logic_ms_1__logic_ms_1__s_in_5.F'], o='logic_ms_1__logic_ms_1__cell_8__aFbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__b.T', 'logic_ms_1__logic_ms_1__s_in_5.F'], o='logic_ms_1__logic_ms_1__cell_8__aFbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__b.T', 'logic_ms_1__logic_ms_1__s_in_5.F'], o='logic_ms_1__logic_ms_1__cell_8__aFbT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__b.F', 'logic_ms_1__logic_ms_1__s_in_5.T'], o='logic_ms_1__logic_ms_1__cell_8__aTbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__b.F', 'logic_ms_1__logic_ms_1__s_in_5.T'], o='logic_ms_1__logic_ms_1__cell_8__aTbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__b.T', 'logic_ms_1__logic_ms_1__s_in_5.T'], o='logic_ms_1__logic_ms_1__cell_8__aTbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__b.T', 'logic_ms_1__logic_ms_1__s_in_5.T'], o='logic_ms_1__logic_ms_1__cell_8__aTbT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_8__aFbF', 'logic_ms_1__logic_ms_1__cell_8__aTbT'], o='logic_ms_1__logic_ms_1__cell_8__x.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_8__aFbF', 'logic_ms_1__logic_ms_1__cell_8__aTbT'], o='logic_ms_1__logic_ms_1__cell_8__x.F', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_8__aTbF', 'logic_ms_1__logic_ms_1__cell_8__aFbT'], o='logic_ms_1__logic_ms_1__cell_8__x.T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_8__aTbF', 'logic_ms_1__logic_ms_1__cell_8__aFbT'], o='logic_ms_1__logic_ms_1__cell_8__x.T', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ms_1__logic_ms_1__cell_8__b.T', 'logic_ms_1__logic_ms_1__s_in_5.T'], o='logic_ms_1__logic_ms_1__cell_8__y.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ms_1__logic_ms_1__cell_8__b.T', 'logic_ms_1__logic_ms_1__s_in_5.T'], o='logic_ms_1__logic_ms_1__cell_8__y.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_8__b.F', 'logic_ms_1__logic_ms_1__s_in_5.F'], o='logic_ms_1__logic_ms_1__cell_8__y.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_8__b.F', 'logic_ms_1__logic_ms_1__s_in_5.F'], o='logic_ms_1__logic_ms_1__cell_8__y.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__c_in.F', 'logic_ms_1__logic_ms_1__cell_8__x.F'], o='logic_ms_1__logic_ms_1__cell_8__xFcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__c_in.F', 'logic_ms_1__logic_ms_1__cell_8__x.F'], o='logic_ms_1__logic_ms_1__cell_8__xFcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__c_in.T', 'logic_ms_1__logic_ms_1__cell_8__x.F'], o='logic_ms_1__logic_ms_1__cell_8__xFcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__c_in.T', 'logic_ms_1__logic_ms_1__cell_8__x.F'], o='logic_ms_1__logic_ms_1__cell_8__xFcT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__c_in.F', 'logic_ms_1__logic_ms_1__cell_8__x.T'], o='logic_ms_1__logic_ms_1__cell_8__xTcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__c_in.F', 'logic_ms_1__logic_ms_1__cell_8__x.T'], o='logic_ms_1__logic_ms_1__cell_8__xTcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__c_in.T', 'logic_ms_1__logic_ms_1__cell_8__x.T'], o='logic_ms_1__logic_ms_1__cell_8__xTcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__c_in.T', 'logic_ms_1__logic_ms_1__cell_8__x.T'], o='logic_ms_1__logic_ms_1__cell_8__xTcT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_8__xFcT', 'logic_ms_1__logic_ms_1__cell_8__xTcF'], o='b2__s_in(5).T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_8__xFcT', 'logic_ms_1__logic_ms_1__cell_8__xTcF'], o='b2__s_in(5).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_8__xTcT', 'logic_ms_1__logic_ms_1__cell_8__xFcF'], o='b2__s_in(5).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_8__xTcT', 'logic_ms_1__logic_ms_1__cell_8__xFcF'], o='b2__s_in(5).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ms_1__logic_ms_1__cell_8__c_in.T', 'logic_ms_1__logic_ms_1__cell_8__x.T'], o='logic_ms_1__logic_ms_1__cell_8__z.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ms_1__logic_ms_1__cell_8__c_in.T', 'logic_ms_1__logic_ms_1__cell_8__x.T'], o='logic_ms_1__logic_ms_1__cell_8__z.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_8__c_in.F', 'logic_ms_1__logic_ms_1__cell_8__x.F'], o='logic_ms_1__logic_ms_1__cell_8__z.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_8__c_in.F', 'logic_ms_1__logic_ms_1__cell_8__x.F'], o='logic_ms_1__logic_ms_1__cell_8__z.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__y.F', 'logic_ms_1__logic_ms_1__cell_8__z.F'], o='b2__s_in(6).F', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__y.F', 'logic_ms_1__logic_ms_1__cell_8__z.F'], o='b2__s_in(6).F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__z.T', 'logic_ms_1__logic_ms_1__cell_8__y.F'], o='logic_ms_1__logic_ms_1__cell_8__yFzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__z.T', 'logic_ms_1__logic_ms_1__cell_8__y.F'], o='logic_ms_1__logic_ms_1__cell_8__yFzT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__y.T', 'logic_ms_1__logic_ms_1__cell_8__z.F'], o='logic_ms_1__logic_ms_1__cell_8__yTzF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__y.T', 'logic_ms_1__logic_ms_1__cell_8__z.F'], o='logic_ms_1__logic_ms_1__cell_8__yTzF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ms_1__logic_ms_1__cell_8__z.T', 'logic_ms_1__logic_ms_1__cell_8__y.T'], o='logic_ms_1__logic_ms_1__cell_8__yTzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ms_1__logic_ms_1__cell_8__z.T', 'logic_ms_1__logic_ms_1__cell_8__y.T'], o='logic_ms_1__logic_ms_1__cell_8__yTzT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ms_1__logic_ms_1__cell_8__yTzF', 'logic_ms_1__logic_ms_1__cell_8__yTzT', 'logic_ms_1__logic_ms_1__cell_8__yFzT'], o='b2__s_in(6).T', d=3.5)
	tr.fall(f=tr.ORf, i=['logic_ms_1__logic_ms_1__cell_8__yTzF', 'logic_ms_1__logic_ms_1__cell_8__yTzT', 'logic_ms_1__logic_ms_1__cell_8__yFzT'], o='b2__s_in(6).T', d=3.5)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_5__b.F', 'logic_ls__logic_ls__cell_5__b.T'], o='logic_ls__logic_ls__done', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_5__b.F', 'logic_ls__logic_ls__cell_5__b.T'], o='logic_ls__logic_ls__done', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__a_in(1).T'], o='logic_ls__logic_ls__cell_6__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__a_in(1).T'], o='logic_ls__logic_ls__cell_6__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__b_in.F', 'logic_ls__logic_ls__a_in(1).F'], o='logic_ls__logic_ls__cell_6__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__b_in.F', 'logic_ls__logic_ls__a_in(1).F'], o='logic_ls__logic_ls__cell_6__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__a_in(2).T'], o='logic_ls__logic_ls__cell_7__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__a_in(2).T'], o='logic_ls__logic_ls__cell_7__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__b_in.F', 'logic_ls__logic_ls__a_in(2).F'], o='logic_ls__logic_ls__cell_7__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__b_in.F', 'logic_ls__logic_ls__a_in(2).F'], o='logic_ls__logic_ls__cell_7__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__a_in(3).T'], o='logic_ls__logic_ls__cell_8__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__a_in(3).T'], o='logic_ls__logic_ls__cell_8__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__b_in.F', 'logic_ls__logic_ls__a_in(3).F'], o='logic_ls__logic_ls__cell_8__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__b_in.F', 'logic_ls__logic_ls__a_in(3).F'], o='logic_ls__logic_ls__cell_8__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__a_in(0).T'], o='logic_ls__logic_ls__cell_5__b.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__b_in.T', 'logic_ls__logic_ls__a_in(0).T'], o='logic_ls__logic_ls__cell_5__b.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__a_in(0).F', 'logic_ls__logic_ls__b_in.F'], o='logic_ls__logic_ls__cell_5__b.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__a_in(0).F', 'logic_ls__logic_ls__b_in.F'], o='logic_ls__logic_ls__cell_5__b.F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__s_in_3.T', 'logic_ls__logic_ls__cell_5__b.T'], o='logic_ls__logic_ls__cell_6__c_in.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__s_in_3.T', 'logic_ls__logic_ls__cell_5__b.T'], o='logic_ls__logic_ls__cell_6__c_in.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_5__b.F', 'logic_ls__logic_ls__s_in_3.F'], o='logic_ls__logic_ls__cell_6__c_in.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_5__b.F', 'logic_ls__logic_ls__s_in_3.F'], o='logic_ls__logic_ls__cell_6__c_in.F', d=3.0)

	tr.rise(f=tr.NANDr, i=['logic_ls__logic_ls__cell_5__b.T', 'logic_ls__logic_ls__s_in_3.F'], o='logic_ls__logic_ls__cell_5__nandFT', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ls__logic_ls__cell_5__b.T', 'logic_ls__logic_ls__s_in_3.F'], o='logic_ls__logic_ls__cell_5__nandFT', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ls__logic_ls__cell_5__b.F', 'logic_ls__logic_ls__s_in_3.T'], o='logic_ls__logic_ls__cell_5__nandTF', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ls__logic_ls__cell_5__b.F', 'logic_ls__logic_ls__s_in_3.T'], o='logic_ls__logic_ls__cell_5__nandTF', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ls__logic_ls__cell_5__nandFT', 'logic_ls__logic_ls__cell_5__nandTF'], o='b3__s_in(3).T', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ls__logic_ls__cell_5__nandFT', 'logic_ls__logic_ls__cell_5__nandTF'], o='b3__s_in(3).T', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ls__logic_ls__s_in_3.T', 'logic_ls__logic_ls__cell_5__b.T'], o='logic_ls__logic_ls__cell_5__nandTT', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ls__logic_ls__s_in_3.T', 'logic_ls__logic_ls__cell_5__b.T'], o='logic_ls__logic_ls__cell_5__nandTT', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ls__logic_ls__cell_5__b.F', 'logic_ls__logic_ls__s_in_3.F'], o='logic_ls__logic_ls__cell_5__nandFF', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ls__logic_ls__cell_5__b.F', 'logic_ls__logic_ls__s_in_3.F'], o='logic_ls__logic_ls__cell_5__nandFF', d=2.0)

	tr.rise(f=tr.NANDr, i=['logic_ls__logic_ls__cell_5__nandFF', 'logic_ls__logic_ls__cell_5__nandTT'], o='b3__s_in(3).F', d=2.0)
	tr.fall(f=tr.NANDf, i=['logic_ls__logic_ls__cell_5__nandFF', 'logic_ls__logic_ls__cell_5__nandTT'], o='b3__s_in(3).F', d=2.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__b.F', 'logic_ls__logic_ls__s_in_4.F'], o='logic_ls__logic_ls__cell_6__aFbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__b.F', 'logic_ls__logic_ls__s_in_4.F'], o='logic_ls__logic_ls__cell_6__aFbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__b.T', 'logic_ls__logic_ls__s_in_4.F'], o='logic_ls__logic_ls__cell_6__aFbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__b.T', 'logic_ls__logic_ls__s_in_4.F'], o='logic_ls__logic_ls__cell_6__aFbT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__b.F', 'logic_ls__logic_ls__s_in_4.T'], o='logic_ls__logic_ls__cell_6__aTbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__b.F', 'logic_ls__logic_ls__s_in_4.T'], o='logic_ls__logic_ls__cell_6__aTbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__b.T', 'logic_ls__logic_ls__s_in_4.T'], o='logic_ls__logic_ls__cell_6__aTbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__b.T', 'logic_ls__logic_ls__s_in_4.T'], o='logic_ls__logic_ls__cell_6__aTbT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_6__aFbF', 'logic_ls__logic_ls__cell_6__aTbT'], o='logic_ls__logic_ls__cell_6__x.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_6__aFbF', 'logic_ls__logic_ls__cell_6__aTbT'], o='logic_ls__logic_ls__cell_6__x.F', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_6__aTbF', 'logic_ls__logic_ls__cell_6__aFbT'], o='logic_ls__logic_ls__cell_6__x.T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_6__aTbF', 'logic_ls__logic_ls__cell_6__aFbT'], o='logic_ls__logic_ls__cell_6__x.T', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__cell_6__b.T', 'logic_ls__logic_ls__s_in_4.T'], o='logic_ls__logic_ls__cell_6__y.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__cell_6__b.T', 'logic_ls__logic_ls__s_in_4.T'], o='logic_ls__logic_ls__cell_6__y.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_6__b.F', 'logic_ls__logic_ls__s_in_4.F'], o='logic_ls__logic_ls__cell_6__y.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_6__b.F', 'logic_ls__logic_ls__s_in_4.F'], o='logic_ls__logic_ls__cell_6__y.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__c_in.F', 'logic_ls__logic_ls__cell_6__x.F'], o='logic_ls__logic_ls__cell_6__xFcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__c_in.F', 'logic_ls__logic_ls__cell_6__x.F'], o='logic_ls__logic_ls__cell_6__xFcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__c_in.T', 'logic_ls__logic_ls__cell_6__x.F'], o='logic_ls__logic_ls__cell_6__xFcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__c_in.T', 'logic_ls__logic_ls__cell_6__x.F'], o='logic_ls__logic_ls__cell_6__xFcT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__c_in.F', 'logic_ls__logic_ls__cell_6__x.T'], o='logic_ls__logic_ls__cell_6__xTcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__c_in.F', 'logic_ls__logic_ls__cell_6__x.T'], o='logic_ls__logic_ls__cell_6__xTcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__c_in.T', 'logic_ls__logic_ls__cell_6__x.T'], o='logic_ls__logic_ls__cell_6__xTcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__c_in.T', 'logic_ls__logic_ls__cell_6__x.T'], o='logic_ls__logic_ls__cell_6__xTcT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_6__xTcF', 'logic_ls__logic_ls__cell_6__xFcT'], o='b3__s_in(4).T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_6__xTcF', 'logic_ls__logic_ls__cell_6__xFcT'], o='b3__s_in(4).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_6__xTcT', 'logic_ls__logic_ls__cell_6__xFcF'], o='b3__s_in(4).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_6__xTcT', 'logic_ls__logic_ls__cell_6__xFcF'], o='b3__s_in(4).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__cell_6__c_in.T', 'logic_ls__logic_ls__cell_6__x.T'], o='logic_ls__logic_ls__cell_6__z.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__cell_6__c_in.T', 'logic_ls__logic_ls__cell_6__x.T'], o='logic_ls__logic_ls__cell_6__z.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_6__c_in.F', 'logic_ls__logic_ls__cell_6__x.F'], o='logic_ls__logic_ls__cell_6__z.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_6__c_in.F', 'logic_ls__logic_ls__cell_6__x.F'], o='logic_ls__logic_ls__cell_6__z.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__y.F', 'logic_ls__logic_ls__cell_6__z.F'], o='logic_ls__logic_ls__cell_7__c_in.F', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__y.F', 'logic_ls__logic_ls__cell_6__z.F'], o='logic_ls__logic_ls__cell_7__c_in.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__z.T', 'logic_ls__logic_ls__cell_6__y.F'], o='logic_ls__logic_ls__cell_6__yFzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__z.T', 'logic_ls__logic_ls__cell_6__y.F'], o='logic_ls__logic_ls__cell_6__yFzT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__z.F', 'logic_ls__logic_ls__cell_6__y.T'], o='logic_ls__logic_ls__cell_6__yTzF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__z.F', 'logic_ls__logic_ls__cell_6__y.T'], o='logic_ls__logic_ls__cell_6__yTzF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_6__z.T', 'logic_ls__logic_ls__cell_6__y.T'], o='logic_ls__logic_ls__cell_6__yTzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_6__z.T', 'logic_ls__logic_ls__cell_6__y.T'], o='logic_ls__logic_ls__cell_6__yTzT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_6__yFzT', 'logic_ls__logic_ls__cell_6__yTzT', 'logic_ls__logic_ls__cell_6__yTzF'], o='logic_ls__logic_ls__cell_7__c_in.T', d=3.5)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_6__yFzT', 'logic_ls__logic_ls__cell_6__yTzT', 'logic_ls__logic_ls__cell_6__yTzF'], o='logic_ls__logic_ls__cell_7__c_in.T', d=3.5)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__b.F', 'logic_ls__logic_ls__s_in_5.F'], o='logic_ls__logic_ls__cell_7__aFbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__b.F', 'logic_ls__logic_ls__s_in_5.F'], o='logic_ls__logic_ls__cell_7__aFbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__b.T', 'logic_ls__logic_ls__s_in_5.F'], o='logic_ls__logic_ls__cell_7__aFbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__b.T', 'logic_ls__logic_ls__s_in_5.F'], o='logic_ls__logic_ls__cell_7__aFbT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__b.F', 'logic_ls__logic_ls__s_in_5.T'], o='logic_ls__logic_ls__cell_7__aTbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__b.F', 'logic_ls__logic_ls__s_in_5.T'], o='logic_ls__logic_ls__cell_7__aTbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__b.T', 'logic_ls__logic_ls__s_in_5.T'], o='logic_ls__logic_ls__cell_7__aTbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__b.T', 'logic_ls__logic_ls__s_in_5.T'], o='logic_ls__logic_ls__cell_7__aTbT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_7__aTbT', 'logic_ls__logic_ls__cell_7__aFbF'], o='logic_ls__logic_ls__cell_7__x.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_7__aTbT', 'logic_ls__logic_ls__cell_7__aFbF'], o='logic_ls__logic_ls__cell_7__x.F', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_7__aFbT', 'logic_ls__logic_ls__cell_7__aTbF'], o='logic_ls__logic_ls__cell_7__x.T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_7__aFbT', 'logic_ls__logic_ls__cell_7__aTbF'], o='logic_ls__logic_ls__cell_7__x.T', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__cell_7__b.T', 'logic_ls__logic_ls__s_in_5.T'], o='logic_ls__logic_ls__cell_7__y.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__cell_7__b.T', 'logic_ls__logic_ls__s_in_5.T'], o='logic_ls__logic_ls__cell_7__y.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_7__b.F', 'logic_ls__logic_ls__s_in_5.F'], o='logic_ls__logic_ls__cell_7__y.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_7__b.F', 'logic_ls__logic_ls__s_in_5.F'], o='logic_ls__logic_ls__cell_7__y.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__c_in.F', 'logic_ls__logic_ls__cell_7__x.F'], o='logic_ls__logic_ls__cell_7__xFcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__c_in.F', 'logic_ls__logic_ls__cell_7__x.F'], o='logic_ls__logic_ls__cell_7__xFcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__c_in.T', 'logic_ls__logic_ls__cell_7__x.F'], o='logic_ls__logic_ls__cell_7__xFcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__c_in.T', 'logic_ls__logic_ls__cell_7__x.F'], o='logic_ls__logic_ls__cell_7__xFcT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__x.T', 'logic_ls__logic_ls__cell_7__c_in.F'], o='logic_ls__logic_ls__cell_7__xTcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__x.T', 'logic_ls__logic_ls__cell_7__c_in.F'], o='logic_ls__logic_ls__cell_7__xTcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__c_in.T', 'logic_ls__logic_ls__cell_7__x.T'], o='logic_ls__logic_ls__cell_7__xTcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__c_in.T', 'logic_ls__logic_ls__cell_7__x.T'], o='logic_ls__logic_ls__cell_7__xTcT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_7__xTcF', 'logic_ls__logic_ls__cell_7__xFcT'], o='b3__s_in(5).T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_7__xTcF', 'logic_ls__logic_ls__cell_7__xFcT'], o='b3__s_in(5).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_7__xTcT', 'logic_ls__logic_ls__cell_7__xFcF'], o='b3__s_in(5).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_7__xTcT', 'logic_ls__logic_ls__cell_7__xFcF'], o='b3__s_in(5).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__cell_7__c_in.T', 'logic_ls__logic_ls__cell_7__x.T'], o='logic_ls__logic_ls__cell_7__z.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__cell_7__c_in.T', 'logic_ls__logic_ls__cell_7__x.T'], o='logic_ls__logic_ls__cell_7__z.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_7__c_in.F', 'logic_ls__logic_ls__cell_7__x.F'], o='logic_ls__logic_ls__cell_7__z.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_7__c_in.F', 'logic_ls__logic_ls__cell_7__x.F'], o='logic_ls__logic_ls__cell_7__z.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__y.F', 'logic_ls__logic_ls__cell_7__z.F'], o='logic_ls__logic_ls__cell_8__c_in.F', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__y.F', 'logic_ls__logic_ls__cell_7__z.F'], o='logic_ls__logic_ls__cell_8__c_in.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__z.T', 'logic_ls__logic_ls__cell_7__y.F'], o='logic_ls__logic_ls__cell_7__yFzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__z.T', 'logic_ls__logic_ls__cell_7__y.F'], o='logic_ls__logic_ls__cell_7__yFzT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__z.F', 'logic_ls__logic_ls__cell_7__y.T'], o='logic_ls__logic_ls__cell_7__yTzF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__z.F', 'logic_ls__logic_ls__cell_7__y.T'], o='logic_ls__logic_ls__cell_7__yTzF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_7__z.T', 'logic_ls__logic_ls__cell_7__y.T'], o='logic_ls__logic_ls__cell_7__yTzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_7__z.T', 'logic_ls__logic_ls__cell_7__y.T'], o='logic_ls__logic_ls__cell_7__yTzT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_7__yFzT', 'logic_ls__logic_ls__cell_7__yTzF', 'logic_ls__logic_ls__cell_7__yTzT'], o='logic_ls__logic_ls__cell_8__c_in.T', d=3.5)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_7__yFzT', 'logic_ls__logic_ls__cell_7__yTzF', 'logic_ls__logic_ls__cell_7__yTzT'], o='logic_ls__logic_ls__cell_8__c_in.T', d=3.5)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__s_in_6.F', 'logic_ls__logic_ls__cell_8__b.F'], o='logic_ls__logic_ls__cell_8__aFbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__s_in_6.F', 'logic_ls__logic_ls__cell_8__b.F'], o='logic_ls__logic_ls__cell_8__aFbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__s_in_6.F', 'logic_ls__logic_ls__cell_8__b.T'], o='logic_ls__logic_ls__cell_8__aFbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__s_in_6.F', 'logic_ls__logic_ls__cell_8__b.T'], o='logic_ls__logic_ls__cell_8__aFbT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__b.F', 'logic_ls__logic_ls__s_in_6.T'], o='logic_ls__logic_ls__cell_8__aTbF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__b.F', 'logic_ls__logic_ls__s_in_6.T'], o='logic_ls__logic_ls__cell_8__aTbF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__b.T', 'logic_ls__logic_ls__s_in_6.T'], o='logic_ls__logic_ls__cell_8__aTbT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__b.T', 'logic_ls__logic_ls__s_in_6.T'], o='logic_ls__logic_ls__cell_8__aTbT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_8__aFbF', 'logic_ls__logic_ls__cell_8__aTbT'], o='logic_ls__logic_ls__cell_8__x.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_8__aFbF', 'logic_ls__logic_ls__cell_8__aTbT'], o='logic_ls__logic_ls__cell_8__x.F', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_8__aTbF', 'logic_ls__logic_ls__cell_8__aFbT'], o='logic_ls__logic_ls__cell_8__x.T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_8__aTbF', 'logic_ls__logic_ls__cell_8__aFbT'], o='logic_ls__logic_ls__cell_8__x.T', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__cell_8__b.T', 'logic_ls__logic_ls__s_in_6.T'], o='logic_ls__logic_ls__cell_8__y.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__cell_8__b.T', 'logic_ls__logic_ls__s_in_6.T'], o='logic_ls__logic_ls__cell_8__y.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__s_in_6.F', 'logic_ls__logic_ls__cell_8__b.F'], o='logic_ls__logic_ls__cell_8__y.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__s_in_6.F', 'logic_ls__logic_ls__cell_8__b.F'], o='logic_ls__logic_ls__cell_8__y.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__x.F', 'logic_ls__logic_ls__cell_8__c_in.F'], o='logic_ls__logic_ls__cell_8__xFcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__x.F', 'logic_ls__logic_ls__cell_8__c_in.F'], o='logic_ls__logic_ls__cell_8__xFcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__x.F', 'logic_ls__logic_ls__cell_8__c_in.T'], o='logic_ls__logic_ls__cell_8__xFcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__x.F', 'logic_ls__logic_ls__cell_8__c_in.T'], o='logic_ls__logic_ls__cell_8__xFcT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__x.T', 'logic_ls__logic_ls__cell_8__c_in.F'], o='logic_ls__logic_ls__cell_8__xTcF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__x.T', 'logic_ls__logic_ls__cell_8__c_in.F'], o='logic_ls__logic_ls__cell_8__xTcF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__x.T', 'logic_ls__logic_ls__cell_8__c_in.T'], o='logic_ls__logic_ls__cell_8__xTcT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__x.T', 'logic_ls__logic_ls__cell_8__c_in.T'], o='logic_ls__logic_ls__cell_8__xTcT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_8__xTcF', 'logic_ls__logic_ls__cell_8__xFcT'], o='b3__s_in(6).T', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_8__xTcF', 'logic_ls__logic_ls__cell_8__xFcT'], o='b3__s_in(6).T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_8__xFcF', 'logic_ls__logic_ls__cell_8__xTcT'], o='b3__s_in(6).F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_8__xFcF', 'logic_ls__logic_ls__cell_8__xTcT'], o='b3__s_in(6).F', d=3.0)

	tr.rise(f=tr.ANDr, i=['logic_ls__logic_ls__cell_8__x.T', 'logic_ls__logic_ls__cell_8__c_in.T'], o='logic_ls__logic_ls__cell_8__z.T', d=3.0)
	tr.fall(f=tr.ANDf, i=['logic_ls__logic_ls__cell_8__x.T', 'logic_ls__logic_ls__cell_8__c_in.T'], o='logic_ls__logic_ls__cell_8__z.T', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_8__x.F', 'logic_ls__logic_ls__cell_8__c_in.F'], o='logic_ls__logic_ls__cell_8__z.F', d=3.0)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_8__x.F', 'logic_ls__logic_ls__cell_8__c_in.F'], o='logic_ls__logic_ls__cell_8__z.F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__y.F', 'logic_ls__logic_ls__cell_8__z.F'], o='b3__s_in(7).F', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__y.F', 'logic_ls__logic_ls__cell_8__z.F'], o='b3__s_in(7).F', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__y.F', 'logic_ls__logic_ls__cell_8__z.T'], o='logic_ls__logic_ls__cell_8__yFzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__y.F', 'logic_ls__logic_ls__cell_8__z.T'], o='logic_ls__logic_ls__cell_8__yFzT', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__y.T', 'logic_ls__logic_ls__cell_8__z.F'], o='logic_ls__logic_ls__cell_8__yTzF', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__y.T', 'logic_ls__logic_ls__cell_8__z.F'], o='logic_ls__logic_ls__cell_8__yTzF', d=3.0)

	tr.rise(f=tr.Cr, i=['logic_ls__logic_ls__cell_8__y.T', 'logic_ls__logic_ls__cell_8__z.T'], o='logic_ls__logic_ls__cell_8__yTzT', d=3.0)
	tr.fall(f=tr.Cf, i=['logic_ls__logic_ls__cell_8__y.T', 'logic_ls__logic_ls__cell_8__z.T'], o='logic_ls__logic_ls__cell_8__yTzT', d=3.0)

	tr.rise(f=tr.ORr, i=['logic_ls__logic_ls__cell_8__yTzT', 'logic_ls__logic_ls__cell_8__yTzF', 'logic_ls__logic_ls__cell_8__yFzT'], o='b3__s_in(7).T', d=3.5)
	tr.fall(f=tr.ORf, i=['logic_ls__logic_ls__cell_8__yTzT', 'logic_ls__logic_ls__cell_8__yTzF', 'logic_ls__logic_ls__cell_8__yFzT'], o='b3__s_in(7).T', d=3.5)

	init = {
	'a(0).T' : 0,
	'a(1).F' : 0,
	'a(3).T' : 0,
	'a(2).F' : 0,
	'a(0).F' : 0,
	'a(2).T' : 0,
	'a(1).T' : 0,
	'a(3).F' : 0,
	'b(3).T' : 0,
	'b(1).T' : 0,
	'b(3).F' : 0,
	'b(0).T' : 0,
	'b(0).F' : 0,
	'b(2).F' : 0,
	'b(2).T' : 0,
	'b(1).F' : 0,
	'ack_in' : 0,
	's(1).T' : 0,
	's(0).T' : 0,
	's(6).T' : 0,
	's(2).F' : 0,
	's(6).F' : 0,
	's(3).F' : 0,
	's(2).T' : 0,
	's(5).T' : 0,
	's(4).T' : 0,
	's(7).T' : 0,
	's(3).T' : 0,
	's(7).F' : 0,
	's(5).F' : 0,
	's(0).F' : 0,
	's(4).F' : 0,
	's(1).F' : 0,
	'logic_fs__logic_fs__b_in_0.T' : 0,
	'logic_fs__logic_fs__b_in_0.F' : 0,
	'logic_fs__logic_fs__b_in_1.T' : 0,
	'logic_fs__logic_fs__b_in_1.F' : 0,
	'logic_ms_1__logic_ms_1__b_in_0.T' : 0,
	'logic_ms_1__logic_ms_1__b_in_0.F' : 0,
	'logic_ms_1__logic_ms_1__s_in_2.T' : 0,
	'logic_ms_1__logic_ms_1__s_in_2.F' : 0,
	'logic_ls__logic_ls__a_in(0).F' : 0,
	'logic_ls__logic_ls__a_in(0).T' : 0,
	'logic_ls__logic_ls__a_in(1).F' : 0,
	'logic_ls__logic_ls__a_in(1).T' : 0,
	'logic_ls__logic_ls__a_in(2).T' : 0,
	'logic_ls__logic_ls__a_in(2).F' : 0,
	'logic_ls__logic_ls__a_in(3).T' : 0,
	'logic_ls__logic_ls__a_in(3).F' : 0,
	'logic_ls__logic_ls__b_in.T' : 0,
	'logic_ls__logic_ls__b_in.F' : 0,
	'logic_ls__logic_ls__s_in_3.T' : 0,
	'logic_ls__logic_ls__s_in_3.F' : 0,
	'b1__a_in(0).F' : 0,
	'b1__a_in(0).T' : 0,
	'b1__a_in(1).F' : 0,
	'b1__a_in(1).T' : 0,
	'b1__a_in(2).F' : 0,
	'b1__a_in(2).T' : 0,
	'b1__a_in(3).T' : 0,
	'b1__a_in(3).F' : 0,
	'b0__c_b_out_0' : 1,
	'b0__c_b_out_1' : 1,
	'b1__b_in(0).F' : 0,
	'b1__b_in(0).T' : 0,
	'b1__b_in(1).F' : 0,
	'b1__b_in(1).T' : 0,
	'b0__ocd_n_lvl0_2' : 1,
	'b2__a_in(0).F' : 0,
	'b2__a_in(0).T' : 0,
	'b2__a_in(1).T' : 0,
	'b2__a_in(1).F' : 0,
	'b2__a_in(2).T' : 0,
	'b2__a_in(2).F' : 0,
	'b2__a_in(3).T' : 0,
	'b2__a_in(3).F' : 0,
	'b1__c_b_out_0' : 1,
	'b2__b_in.F' : 0,
	'b2__b_in.T' : 0,
	'b2__s_in(0).T' : 0,
	'b2__s_in(0).F' : 0,
	'b1__s_in(0).F' : 0,
	'b1__s_in(0).T' : 0,
	'b2__s_in(1).F' : 0,
	'b2__s_in(1).T' : 0,
	'b1__c_s_out_2' : 1,
	'logic_ms_1__logic_ms_1__s_in_3.F' : 0,
	'logic_ms_1__logic_ms_1__s_in_3.T' : 0,
	'logic_ms_1__logic_ms_1__s_in_4.F' : 0,
	'logic_ms_1__logic_ms_1__s_in_4.T' : 0,
	'logic_ms_1__logic_ms_1__s_in_5.T' : 0,
	'logic_ms_1__logic_ms_1__s_in_5.F' : 0,
	'b2__c_a_out_0' : 1,
	'b2__c_a_out_1' : 1,
	'b2__c_a_out_2' : 1,
	'b2__c_a_out_3' : 1,
	'b2__c_b_out' : 1,
	'b3__s_in(0).T' : 0,
	'b3__s_in(0).F' : 0,
	'b3__s_in(1).T' : 0,
	'b3__s_in(1).F' : 0,
	'b3__s_in(2).F' : 0,
	'b3__s_in(2).T' : 0,
	'b2__c_s_out_3' : 1,
	'logic_ls__logic_ls__s_in_4.F' : 0,
	'logic_ls__logic_ls__s_in_4.T' : 0,
	'logic_ls__logic_ls__s_in_5.T' : 0,
	'logic_ls__logic_ls__s_in_5.F' : 0,
	'logic_ls__logic_ls__s_in_6.F' : 0,
	'logic_ls__logic_ls__s_in_6.T' : 0,
	'b2__ocd_n_lvl0_0' : 1,
	'b2__ocd_n_lvl0_1' : 1,
	'b2__ocd_n_lvl1_0' : 1,
	'b3__c_s_out_0' : 1,
	'b3__en' : 1,
	'b3__c_s_out_1' : 1,
	'b3__c_s_out_2' : 1,
	'b3__c_s_out_3' : 1,
	'b3__c_s_out_4' : 1,
	'b3__c_s_out_5' : 1,
	'b3__c_s_out_6' : 1,
	'b3__c_s_out_7' : 1,
	'b3__ocd_n_lvl0_0' : 1,
	'b3__ocd_n_lvl0_1' : 1,
	'b3__ocd_n_lvl0_2' : 1,
	'b3__ocd_n_lvl0_3' : 1,
	'b3__ocd_n_lvl1_0' : 1,
	'b3__ocd_n_lvl1_1' : 1,
	'b3__ocd_n' : 1,
	'logic_fs__logic_fs__cell_07__b.T' : 0,
	'logic_fs__logic_fs__cell_07__b.F' : 0,
	'logic_fs__logic_fs__cell_11__a.F' : 0,
	'logic_fs__logic_fs__cell_11__a.T' : 0,
	'logic_fs__logic_fs__cell_11__b.T' : 0,
	'logic_fs__logic_fs__cell_11__b.F' : 0,
	'logic_fs__logic_fs__cell_12__b.T' : 0,
	'logic_fs__logic_fs__cell_12__b.F' : 0,
	'logic_fs__logic_fs__cell_13__b.T' : 0,
	'logic_fs__logic_fs__cell_13__b.F' : 0,
	'logic_fs__logic_fs__cell_12__a.T' : 0,
	'logic_fs__logic_fs__cell_12__a.F' : 0,
	'logic_fs__logic_fs__cell_13__a.T' : 0,
	'logic_fs__logic_fs__cell_13__a.F' : 0,
	'logic_fs__logic_fs__cell_07__nandFT' : 1,
	'logic_fs__logic_fs__cell_07__nandTF' : 1,
	'logic_fs__logic_fs__cell_07__nandTT' : 1,
	'logic_fs__logic_fs__cell_07__nandFF' : 1,
	'logic_fs__logic_fs__cell_12__c_in.T' : 0,
	'logic_fs__logic_fs__cell_12__c_in.F' : 0,
	'logic_fs__logic_fs__cell_11__nandFT' : 1,
	'logic_fs__logic_fs__cell_11__nandTF' : 1,
	'logic_fs__logic_fs__cell_11__nandTT' : 1,
	'logic_fs__logic_fs__cell_11__nandFF' : 1,
	'logic_fs__logic_fs__cell_12__aFbF' : 0,
	'logic_fs__logic_fs__cell_12__aFbT' : 0,
	'logic_fs__logic_fs__cell_12__aTbF' : 0,
	'logic_fs__logic_fs__cell_12__aTbT' : 0,
	'logic_fs__logic_fs__cell_12__x.F' : 0,
	'logic_fs__logic_fs__cell_12__x.T' : 0,
	'logic_fs__logic_fs__cell_12__y.T' : 0,
	'logic_fs__logic_fs__cell_12__y.F' : 0,
	'logic_fs__logic_fs__cell_12__xFcF' : 0,
	'logic_fs__logic_fs__cell_12__xFcT' : 0,
	'logic_fs__logic_fs__cell_12__xTcF' : 0,
	'logic_fs__logic_fs__cell_12__xTcT' : 0,
	'logic_fs__logic_fs__cell_12__z.T' : 0,
	'logic_fs__logic_fs__cell_12__z.F' : 0,
	'logic_fs__logic_fs__cell_13__c_in.F' : 0,
	'logic_fs__logic_fs__cell_12__yFzT' : 0,
	'logic_fs__logic_fs__cell_12__yTzF' : 0,
	'logic_fs__logic_fs__cell_12__yTzT' : 0,
	'logic_fs__logic_fs__cell_13__c_in.T' : 0,
	'logic_fs__logic_fs__cell_13__aFbF' : 0,
	'logic_fs__logic_fs__cell_13__aFbT' : 0,
	'logic_fs__logic_fs__cell_13__aTbF' : 0,
	'logic_fs__logic_fs__cell_13__aTbT' : 0,
	'logic_fs__logic_fs__cell_13__x.F' : 0,
	'logic_fs__logic_fs__cell_13__x.T' : 0,
	'logic_fs__logic_fs__cell_13__y.T' : 0,
	'logic_fs__logic_fs__cell_13__y.F' : 0,
	'logic_fs__logic_fs__cell_13__xFcF' : 0,
	'logic_fs__logic_fs__cell_13__xFcT' : 0,
	'logic_fs__logic_fs__cell_13__xTcF' : 0,
	'logic_fs__logic_fs__cell_13__xTcT' : 0,
	'logic_fs__logic_fs__cell_13__z.T' : 0,
	'logic_fs__logic_fs__cell_13__z.F' : 0,
	'logic_fs__logic_fs__cell_13__yFzT' : 0,
	'logic_fs__logic_fs__cell_13__yTzF' : 0,
	'logic_fs__logic_fs__cell_13__yTzT' : 0,
	'logic_ms_1__logic_ms_1__cell_5__b.T' : 0,
	'logic_ms_1__logic_ms_1__cell_5__b.F' : 0,
	'logic_ms_1__logic_ms_1__cell_6__b.T' : 0,
	'logic_ms_1__logic_ms_1__cell_6__b.F' : 0,
	'logic_ms_1__logic_ms_1__cell_7__b.T' : 0,
	'logic_ms_1__logic_ms_1__cell_7__b.F' : 0,
	'logic_ms_1__logic_ms_1__cell_8__b.T' : 0,
	'logic_ms_1__logic_ms_1__cell_8__b.F' : 0,
	'logic_ms_1__logic_ms_1__cell_6__c_in.T' : 0,
	'logic_ms_1__logic_ms_1__cell_6__c_in.F' : 0,
	'logic_ms_1__logic_ms_1__cell_5__nandFT' : 1,
	'logic_ms_1__logic_ms_1__cell_5__nandTF' : 1,
	'logic_ms_1__logic_ms_1__cell_5__nandTT' : 1,
	'logic_ms_1__logic_ms_1__cell_5__nandFF' : 1,
	'logic_ms_1__logic_ms_1__cell_6__aFbF' : 0,
	'logic_ms_1__logic_ms_1__cell_6__aFbT' : 0,
	'logic_ms_1__logic_ms_1__cell_6__aTbF' : 0,
	'logic_ms_1__logic_ms_1__cell_6__aTbT' : 0,
	'logic_ms_1__logic_ms_1__cell_6__x.F' : 0,
	'logic_ms_1__logic_ms_1__cell_6__x.T' : 0,
	'logic_ms_1__logic_ms_1__cell_6__y.T' : 0,
	'logic_ms_1__logic_ms_1__cell_6__y.F' : 0,
	'logic_ms_1__logic_ms_1__cell_6__xFcF' : 0,
	'logic_ms_1__logic_ms_1__cell_6__xFcT' : 0,
	'logic_ms_1__logic_ms_1__cell_6__xTcF' : 0,
	'logic_ms_1__logic_ms_1__cell_6__xTcT' : 0,
	'logic_ms_1__logic_ms_1__cell_6__z.T' : 0,
	'logic_ms_1__logic_ms_1__cell_6__z.F' : 0,
	'logic_ms_1__logic_ms_1__cell_7__c_in.F' : 0,
	'logic_ms_1__logic_ms_1__cell_6__yFzT' : 0,
	'logic_ms_1__logic_ms_1__cell_6__yTzF' : 0,
	'logic_ms_1__logic_ms_1__cell_6__yTzT' : 0,
	'logic_ms_1__logic_ms_1__cell_7__c_in.T' : 0,
	'logic_ms_1__logic_ms_1__cell_7__aFbF' : 0,
	'logic_ms_1__logic_ms_1__cell_7__aFbT' : 0,
	'logic_ms_1__logic_ms_1__cell_7__aTbF' : 0,
	'logic_ms_1__logic_ms_1__cell_7__aTbT' : 0,
	'logic_ms_1__logic_ms_1__cell_7__x.F' : 0,
	'logic_ms_1__logic_ms_1__cell_7__x.T' : 0,
	'logic_ms_1__logic_ms_1__cell_7__y.T' : 0,
	'logic_ms_1__logic_ms_1__cell_7__y.F' : 0,
	'logic_ms_1__logic_ms_1__cell_7__xFcF' : 0,
	'logic_ms_1__logic_ms_1__cell_7__xFcT' : 0,
	'logic_ms_1__logic_ms_1__cell_7__xTcF' : 0,
	'logic_ms_1__logic_ms_1__cell_7__xTcT' : 0,
	'logic_ms_1__logic_ms_1__cell_7__z.T' : 0,
	'logic_ms_1__logic_ms_1__cell_7__z.F' : 0,
	'logic_ms_1__logic_ms_1__cell_8__c_in.F' : 0,
	'logic_ms_1__logic_ms_1__cell_7__yFzT' : 0,
	'logic_ms_1__logic_ms_1__cell_7__yTzF' : 0,
	'logic_ms_1__logic_ms_1__cell_7__yTzT' : 0,
	'logic_ms_1__logic_ms_1__cell_8__c_in.T' : 0,
	'logic_ms_1__logic_ms_1__cell_8__aFbF' : 0,
	'logic_ms_1__logic_ms_1__cell_8__aFbT' : 0,
	'logic_ms_1__logic_ms_1__cell_8__aTbF' : 0,
	'logic_ms_1__logic_ms_1__cell_8__aTbT' : 0,
	'logic_ms_1__logic_ms_1__cell_8__x.F' : 0,
	'logic_ms_1__logic_ms_1__cell_8__x.T' : 0,
	'logic_ms_1__logic_ms_1__cell_8__y.T' : 0,
	'logic_ms_1__logic_ms_1__cell_8__y.F' : 0,
	'logic_ms_1__logic_ms_1__cell_8__xFcF' : 0,
	'logic_ms_1__logic_ms_1__cell_8__xFcT' : 0,
	'logic_ms_1__logic_ms_1__cell_8__xTcF' : 0,
	'logic_ms_1__logic_ms_1__cell_8__xTcT' : 0,
	'logic_ms_1__logic_ms_1__cell_8__z.T' : 0,
	'logic_ms_1__logic_ms_1__cell_8__z.F' : 0,
	'logic_ms_1__logic_ms_1__cell_8__yFzT' : 0,
	'logic_ms_1__logic_ms_1__cell_8__yTzF' : 0,
	'logic_ms_1__logic_ms_1__cell_8__yTzT' : 0,
	'logic_ls__logic_ls__cell_5__b.F' : 0,
	'logic_ls__logic_ls__cell_5__b.T' : 0,
	'logic_ls__logic_ls__cell_6__b.T' : 0,
	'logic_ls__logic_ls__cell_6__b.F' : 0,
	'logic_ls__logic_ls__cell_7__b.T' : 0,
	'logic_ls__logic_ls__cell_7__b.F' : 0,
	'logic_ls__logic_ls__cell_8__b.T' : 0,
	'logic_ls__logic_ls__cell_8__b.F' : 0,
	'logic_ls__logic_ls__cell_6__c_in.T' : 0,
	'logic_ls__logic_ls__cell_6__c_in.F' : 0,
	'logic_ls__logic_ls__cell_5__nandFT' : 1,
	'logic_ls__logic_ls__cell_5__nandTF' : 1,
	'logic_ls__logic_ls__cell_5__nandTT' : 1,
	'logic_ls__logic_ls__cell_5__nandFF' : 1,
	'logic_ls__logic_ls__cell_6__aFbF' : 0,
	'logic_ls__logic_ls__cell_6__aFbT' : 0,
	'logic_ls__logic_ls__cell_6__aTbF' : 0,
	'logic_ls__logic_ls__cell_6__aTbT' : 0,
	'logic_ls__logic_ls__cell_6__x.F' : 0,
	'logic_ls__logic_ls__cell_6__x.T' : 0,
	'logic_ls__logic_ls__cell_6__y.T' : 0,
	'logic_ls__logic_ls__cell_6__y.F' : 0,
	'logic_ls__logic_ls__cell_6__xFcF' : 0,
	'logic_ls__logic_ls__cell_6__xFcT' : 0,
	'logic_ls__logic_ls__cell_6__xTcF' : 0,
	'logic_ls__logic_ls__cell_6__xTcT' : 0,
	'logic_ls__logic_ls__cell_6__z.T' : 0,
	'logic_ls__logic_ls__cell_6__z.F' : 0,
	'logic_ls__logic_ls__cell_7__c_in.F' : 0,
	'logic_ls__logic_ls__cell_6__yFzT' : 0,
	'logic_ls__logic_ls__cell_6__yTzF' : 0,
	'logic_ls__logic_ls__cell_6__yTzT' : 0,
	'logic_ls__logic_ls__cell_7__c_in.T' : 0,
	'logic_ls__logic_ls__cell_7__aFbF' : 0,
	'logic_ls__logic_ls__cell_7__aFbT' : 0,
	'logic_ls__logic_ls__cell_7__aTbF' : 0,
	'logic_ls__logic_ls__cell_7__aTbT' : 0,
	'logic_ls__logic_ls__cell_7__x.F' : 0,
	'logic_ls__logic_ls__cell_7__x.T' : 0,
	'logic_ls__logic_ls__cell_7__y.T' : 0,
	'logic_ls__logic_ls__cell_7__y.F' : 0,
	'logic_ls__logic_ls__cell_7__xFcF' : 0,
	'logic_ls__logic_ls__cell_7__xFcT' : 0,
	'logic_ls__logic_ls__cell_7__xTcF' : 0,
	'logic_ls__logic_ls__cell_7__xTcT' : 0,
	'logic_ls__logic_ls__cell_7__z.T' : 0,
	'logic_ls__logic_ls__cell_7__z.F' : 0,
	'logic_ls__logic_ls__cell_8__c_in.F' : 0,
	'logic_ls__logic_ls__cell_7__yFzT' : 0,
	'logic_ls__logic_ls__cell_7__yTzF' : 0,
	'logic_ls__logic_ls__cell_7__yTzT' : 0,
	'logic_ls__logic_ls__cell_8__c_in.T' : 0,
	'logic_ls__logic_ls__cell_8__aFbF' : 0,
	'logic_ls__logic_ls__cell_8__aFbT' : 0,
	'logic_ls__logic_ls__cell_8__aTbF' : 0,
	'logic_ls__logic_ls__cell_8__aTbT' : 0,
	'logic_ls__logic_ls__cell_8__x.F' : 0,
	'logic_ls__logic_ls__cell_8__x.T' : 0,
	'logic_ls__logic_ls__cell_8__y.T' : 0,
	'logic_ls__logic_ls__cell_8__y.F' : 0,
	'logic_ls__logic_ls__cell_8__xFcF' : 0,
	'logic_ls__logic_ls__cell_8__xFcT' : 0,
	'logic_ls__logic_ls__cell_8__xTcF' : 0,
	'logic_ls__logic_ls__cell_8__xTcT' : 0,
	'logic_ls__logic_ls__cell_8__z.T' : 0,
	'logic_ls__logic_ls__cell_8__z.F' : 0,
	'logic_ls__logic_ls__cell_8__yFzT' : 0,
	'logic_ls__logic_ls__cell_8__yTzF' : 0,
	'logic_ls__logic_ls__cell_8__yTzT' : 0,
	'b2__c_s_out_6' : 1,
	'b2__s_in(4).F' : 0,
	'b2__s_in(3).F' : 0,
	'logic_fs_b_in_1__done_n' : 1,
	'b2__c_s_out_0' : 1,
	'b2__s_in(5).F' : 0,
	'b3__s_in(3).T' : 0,
	'b3__s_in(4).T' : 0,
	'b3__s_in(5).T' : 0,
	'logic_ls_a_in_2__done_n' : 1,
	'b3__s_in(6).T' : 0,
	'b1__c_s_out_1' : 1,
	'b1__c_s_out_4' : 1,
	'logic_fs__logic_fs__cell_07__a.T' : 0,
	'b1__c_a_out_1' : 1,
	'b1__s_in(1).F' : 0,
	'b3__s_in(5).F' : 0,
	'b0__c_b_out_3' : 1,
	'b3__s_in(4).F' : 0,
	'b3__s_in(6).F' : 0,
	'logic_ls_a_in_3__done_n' : 1,
	'logic_fs__logic_fs__int_sig_22_done_n' : 1,
	'b0__c_a_out_1' : 1,
	'logic_ms_1__logic_ms_1__done' : 0,
	'b2__s_in(6).T' : 0,
	'b2__c_s_out_5' : 1,
	'b2__c_s_out_2' : 1,
	'b1__s_in(4).T' : 0,
	'logic_fs__logic_fs__cell_07__a.F' : 0,
	'b2__s_in(2).F' : 0,
	'b1__c_s_out_3' : 1,
	'b1__c_s_out_0' : 1,
	'logic_ls_b_in_done_n' : 1,
	'logic_fs__logic_fs__int_sig_23_done_n' : 1,
	'b1__c_a_out_3' : 1,
	'logic_ls__logic_ls__done' : 0,
	'b3__s_in(7).T' : 0,
	'b1__c_a_out_0' : 1,
	'b0__c_b_out_2' : 1,
	'b2__s_in(6).F' : 0,
	'b3__s_in(3).F' : 0,
	'b0__c_a_out_3' : 1,
	'logic_ls__ack_in' : 0,
	'b1__s_in(5).T' : 0,
	'b1__s_in(2).T' : 0,
	'b0__c_a_out_0' : 1,
	'logic_ls_s_in_3__done_n' : 1,
	'logic_ls_a_in_0__done_n' : 1,
	'b1__s_in(1).T' : 0,
	'b1__s_in(3).T' : 0,
	'b2__c_s_out_1' : 1,
	'b2__c_s_out_4' : 1,
	'logic_ms_1_b_in_0__done_n' : 1,
	'b1__c_s_out_5' : 1,
	'b1__c_b_out_1' : 1,
	'b3__s_in(7).F' : 0,
	'b1__s_in(2).F' : 0,
	'b1__c_a_out_2' : 1,
	'logic_fs_b_in_0__done_n' : 1,
	'b1__s_in(5).F' : 0,
	'b1__s_in(3).F' : 0,
	'b2__s_in(2).T' : 0,
	'logic_ls_a_in_1__done_n' : 1,
	'b2__s_in(3).T' : 0,
	'b2__s_in(4).T' : 0,
	'b2__s_in(5).T' : 0,
	'logic_fs__logic_fs__int_sig_20_done_n' : 1,
	'b0__c_a_out_2' : 1,
	'b1__s_in(4).F' : 0,
	'logic_ms_1_s_in_2__done_n' : 1,
	'logic_ls_chin_cd_n_lvl0_1' : 1,
	'b2__ocd_n_lvl0_2' : 1,
	'logic_fs__logic_fs__int_sig_21_done_n' : 1,
	'b2__ocd_n_lvl0_5' : 1,
	'b1__ocd_n_lvl0_1' : 1,
	'b0__ocd_n_lvl0_1' : 1,
	'logic_ms_1_chin_cd_n' : 1,
	'b1__ocd_n_lvl0_4' : 1,
	'logic_fs__logic_fs__internal_done_n_merged_lvl0_0' : 1,
	'logic_ls_chin_cd_n_lvl0_2' : 1,
	'b2__ocd_n_lvl0_3' : 1,
	'b1__ocd_n_lvl0_3' : 1,
	'logic_fs_chin_cd_n' : 1,
	'b1__ocd_n_lvl0_2' : 1,
	'logic_fs__logic_fs__internal_done_n_merged_lvl0_1' : 1,
	'logic_ls_chin_cd_n_lvl0_0' : 1,
	'b1__ocd_n_lvl0_5' : 1,
	'b0__ocd_n_lvl0_0' : 1,
	'b1__ocd_n_lvl0_0' : 1,
	'b2__ocd_n_lvl0_4' : 1,
	'logic_ls__ack_out' : 0,
	'b0__ocd_n_lvl0_3' : 1,
	'b1__ocd_n_lvl1_1' : 1,
	'logic_fs__logic_fs__internal_done_n_merged' : 1,
	'b1__ocd_n_lvl1_0' : 1,
	'logic_ms_1_chin_cd' : 0,
	'b0__ocd_n_lvl1_1' : 1,
	'logic_ls_chin_cd_n_lvl1_0' : 1,
	'logic_fs_chin_cd' : 0,
	'b2__ocd_n_lvl1_2' : 1,
	'b0__ocd_n_lvl1_0' : 1,
	'b1__ocd_n_lvl1_2' : 1,
	'b2__ocd_n_lvl1_1' : 1,
	'b0__ocd_n' : 1,
	'logic_ls_chin_cd_n' : 1,
	'b1__ocd_n_lvl2_0' : 1,
	'b2__ocd_n_lvl2_0' : 1,
	'logic_fs__logic_fs__done' : 0,
	'logic_ls_chin_cd' : 0,
	'b1__ocd_n' : 1,
	'b2__ocd_n' : 1,
	'ack_out' : 0,
	'b2__ack_in' : 0,
	'logic_ms_1__ack_in' : 0,
	'logic_fs__ack_in' : 0,
	'logic_ms_1__ack_out' : 0,
	'logic_fs__ack_out' : 0,
	'b2__en' : 1,
	'b0__ack_in' : 0,
	'b1__ack_in' : 0,
	'b1__en' : 1,
	'b0__en' : 1,
	}

	events = []

	tokens = [{'a': 1, 'b': 14}, {'a': 10, 'b': 10}, {'a': 8, 'b': 5}, {'a': 13, 'b': 4}, {'a': 14, 'b': 6}, {'a': 1, 'b': 3}, {'a': 6, 'b': 5}, {'a': 6, 'b': 11}]

	input_widths = {'a': 4, 'b': 4}

	output_signals = {'s(1).T', 's(3).F', 's(5).T', 'ack_out', 's(4).T', 's(7).T', 's(3).T', 's(0).F', 's(4).F', 's(0).T', 's(6).T', 's(2).F', 's(6).F', 's(2).T', 's(7).F', 's(5).F', 's(1).F'}

	output_widths = {'s': 8}

	return init, events, tokens, input_widths, output_signals, output_widths