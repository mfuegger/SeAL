from seal import tracem as tr

def GeneratePipeline():

	tr.rise(f=tr.NORr, i=['d1__chin_op.T', 'd1__chin_op.F'], o='b1__c_op_out_0', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_op.T', 'd1__chin_op.F'], o='b1__c_op_out_0', d=1.0)

	tr.rise(f=tr.Cr, i=['op(0).F', 'b1__en'], o='d1__chin_op.F', d=1.0)
	tr.fall(f=tr.Cf, i=['op(0).F', 'b1__en'], o='d1__chin_op.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op(0).T', 'b1__en'], o='d1__chin_op.T', d=1.0)
	tr.fall(f=tr.Cf, i=['op(0).T', 'b1__en'], o='d1__chin_op.T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__cntrl_select.T', 'd1__cntrl_select.F'], o='b1__c_op_out_1', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__cntrl_select.T', 'd1__cntrl_select.F'], o='b1__c_op_out_1', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'op(1).F'], o='d1__cntrl_select.F', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'op(1).F'], o='d1__cntrl_select.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op(1).T', 'b1__en'], o='d1__cntrl_select.T', d=1.0)
	tr.fall(f=tr.Cf, i=['op(1).T', 'b1__en'], o='d1__cntrl_select.T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chin_a(0).T', 'd1__chin_a(0).F'], o='b1__c_a_out_0', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_a(0).T', 'd1__chin_a(0).F'], o='b1__c_a_out_0', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'a(0).F'], o='d1__chin_a(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'a(0).F'], o='d1__chin_a(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['a(0).T', 'b1__en'], o='d1__chin_a(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['a(0).T', 'b1__en'], o='d1__chin_a(0).T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chin_a(1).T', 'd1__chin_a(1).F'], o='b1__c_a_out_1', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_a(1).T', 'd1__chin_a(1).F'], o='b1__c_a_out_1', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'a(1).F'], o='d1__chin_a(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'a(1).F'], o='d1__chin_a(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['a(1).T', 'b1__en'], o='d1__chin_a(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['a(1).T', 'b1__en'], o='d1__chin_a(1).T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chin_a(2).F', 'd1__chin_a(2).T'], o='b1__c_a_out_2', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_a(2).F', 'd1__chin_a(2).T'], o='b1__c_a_out_2', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'a(2).F'], o='d1__chin_a(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'a(2).F'], o='d1__chin_a(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'a(2).T'], o='d1__chin_a(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'a(2).T'], o='d1__chin_a(2).T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chin_a(3).F', 'd1__chin_a(3).T'], o='b1__c_a_out_3', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_a(3).F', 'd1__chin_a(3).T'], o='b1__c_a_out_3', d=1.0)

	tr.rise(f=tr.Cr, i=['a(3).F', 'b1__en'], o='d1__chin_a(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['a(3).F', 'b1__en'], o='d1__chin_a(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['a(3).T', 'b1__en'], o='d1__chin_a(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['a(3).T', 'b1__en'], o='d1__chin_a(3).T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chin_b(0).T', 'd1__chin_b(0).F'], o='b1__c_b_out_0', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_b(0).T', 'd1__chin_b(0).F'], o='b1__c_b_out_0', d=1.0)

	tr.rise(f=tr.Cr, i=['b(0).F', 'b1__en'], o='d1__chin_b(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b(0).F', 'b1__en'], o='d1__chin_b(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b(0).T', 'b1__en'], o='d1__chin_b(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b(0).T', 'b1__en'], o='d1__chin_b(0).T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chin_b(1).T', 'd1__chin_b(1).F'], o='b1__c_b_out_1', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_b(1).T', 'd1__chin_b(1).F'], o='b1__c_b_out_1', d=1.0)

	tr.rise(f=tr.Cr, i=['b(1).F', 'b1__en'], o='d1__chin_b(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b(1).F', 'b1__en'], o='d1__chin_b(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__en', 'b(1).T'], o='d1__chin_b(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__en', 'b(1).T'], o='d1__chin_b(1).T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chin_b(2).F', 'd1__chin_b(2).T'], o='b1__c_b_out_2', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_b(2).F', 'd1__chin_b(2).T'], o='b1__c_b_out_2', d=1.0)

	tr.rise(f=tr.Cr, i=['b(2).F', 'b1__en'], o='d1__chin_b(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b(2).F', 'b1__en'], o='d1__chin_b(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b(2).T', 'b1__en'], o='d1__chin_b(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b(2).T', 'b1__en'], o='d1__chin_b(2).T', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chin_b(3).F', 'd1__chin_b(3).T'], o='b1__c_b_out_3', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chin_b(3).F', 'd1__chin_b(3).T'], o='b1__c_b_out_3', d=1.0)

	tr.rise(f=tr.Cr, i=['b(3).F', 'b1__en'], o='d1__chin_b(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b(3).F', 'b1__en'], o='d1__chin_b(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b(3).T', 'b1__en'], o='d1__chin_b(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b(3).T', 'b1__en'], o='d1__chin_b(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__c_op_out_0', 'b1__c_op_out_1'], o='b1__ocd_n_lvl0_0', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__c_op_out_0', 'b1__c_op_out_1'], o='b1__ocd_n_lvl0_0', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__c_a_out_0', 'b1__c_a_out_1'], o='b1__ocd_n_lvl0_1', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__c_a_out_0', 'b1__c_a_out_1'], o='b1__ocd_n_lvl0_1', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__c_a_out_2', 'b1__c_a_out_3'], o='b1__ocd_n_lvl0_2', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__c_a_out_2', 'b1__c_a_out_3'], o='b1__ocd_n_lvl0_2', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__c_b_out_1', 'b1__c_b_out_0'], o='b1__ocd_n_lvl0_3', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__c_b_out_1', 'b1__c_b_out_0'], o='b1__ocd_n_lvl0_3', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__c_b_out_2', 'b1__c_b_out_3'], o='b1__ocd_n_lvl0_4', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__c_b_out_2', 'b1__c_b_out_3'], o='b1__ocd_n_lvl0_4', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_0', 'b1__ocd_n_lvl0_1'], o='b1__ocd_n_lvl1_0', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_0', 'b1__ocd_n_lvl0_1'], o='b1__ocd_n_lvl1_0', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_2', 'b1__ocd_n_lvl0_3'], o='b1__ocd_n_lvl1_1', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_2', 'b1__ocd_n_lvl0_3'], o='b1__ocd_n_lvl1_1', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl1_1', 'b1__ocd_n_lvl1_0'], o='b1__ocd_n_lvl2_0', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl1_1', 'b1__ocd_n_lvl1_0'], o='b1__ocd_n_lvl2_0', d=1.0)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_4', 'b1__ocd_n_lvl2_0'], o='b1__ocd_n', d=1.0)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_4', 'b1__ocd_n_lvl2_0'], o='b1__ocd_n', d=1.0)

	tr.rise(f=tr.INVr, i=['b1__ocd_n'], o='ack_out', d=1.0)
	tr.fall(f=tr.INVf, i=['b1__ocd_n'], o='ack_out', d=1.0)

	tr.rise(f=tr.NORr, i=['z(0).T', 'z(0).F'], o='b2__c_z_out_0', d=1.0)
	tr.fall(f=tr.NORf, i=['z(0).T', 'z(0).F'], o='b2__c_z_out_0', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__z_in(0).F'], o='z(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__z_in(0).F'], o='z(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__z_in(0).T', 'b2__en'], o='z(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__z_in(0).T', 'b2__en'], o='z(0).T', d=1.0)

	tr.rise(f=tr.NORr, i=['z(1).F', 'z(1).T'], o='b2__c_z_out_1', d=1.0)
	tr.fall(f=tr.NORf, i=['z(1).F', 'z(1).T'], o='b2__c_z_out_1', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__z_in(1).F'], o='z(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__z_in(1).F'], o='z(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__z_in(1).T', 'b2__en'], o='z(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__z_in(1).T', 'b2__en'], o='z(1).T', d=1.0)

	tr.rise(f=tr.NORr, i=['z(2).F', 'z(2).T'], o='b2__c_z_out_2', d=1.0)
	tr.fall(f=tr.NORf, i=['z(2).F', 'z(2).T'], o='b2__c_z_out_2', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__z_in(2).F'], o='z(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__z_in(2).F'], o='z(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__z_in(2).T', 'b2__en'], o='z(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__z_in(2).T', 'b2__en'], o='z(2).T', d=1.0)

	tr.rise(f=tr.NORr, i=['z(3).F', 'z(3).T'], o='b2__c_z_out_3', d=1.0)
	tr.fall(f=tr.NORf, i=['z(3).F', 'z(3).T'], o='b2__c_z_out_3', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__z_in(3).F', 'b2__en'], o='z(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__z_in(3).F', 'b2__en'], o='z(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__z_in(3).T', 'b2__en'], o='z(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__z_in(3).T', 'b2__en'], o='z(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__c_z_out_0', 'b2__c_z_out_1'], o='b2__ocd_n_lvl0_0', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__c_z_out_0', 'b2__c_z_out_1'], o='b2__ocd_n_lvl0_0', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__c_z_out_2', 'b2__c_z_out_3'], o='b2__ocd_n_lvl0_1', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__c_z_out_2', 'b2__c_z_out_3'], o='b2__ocd_n_lvl0_1', d=1.0)

	tr.rise(f=tr.Cr, i=['b2__ocd_n_lvl0_1', 'b2__ocd_n_lvl0_0'], o='b2__ocd_n', d=1.0)
	tr.fall(f=tr.Cf, i=['b2__ocd_n_lvl0_1', 'b2__ocd_n_lvl0_0'], o='b2__ocd_n', d=1.0)

	tr.rise(f=tr.INVr, i=['b2__ocd_n'], o='m__chout_ack', d=1.0)
	tr.fall(f=tr.INVf, i=['b2__ocd_n'], o='m__chout_ack', d=1.0)

	tr.rise(f=tr.INVr, i=['ack_in'], o='b2__en', d=1.0)
	tr.fall(f=tr.INVf, i=['ack_in'], o='b2__en', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_a(3).T'], o='op_addsub__op_addsub__a(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_a(3).T'], o='op_addsub__op_addsub__a(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__chin_a(3).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__chin_a(3).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(0).T'], o='op_addsub__op_addsub__b(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(0).T'], o='op_addsub__op_addsub__b(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(0).F'], o='op_addsub__op_addsub__b(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(0).F'], o='op_addsub__op_addsub__b(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__chin_a(1).T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__chin_a(1).T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__chin_a(1).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__chin_a(1).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__chin_op.T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__op.T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__chin_op.T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__op.T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_op.F'], o='op_addsub__op_addsub__op.F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_op.F'], o='op_addsub__op_addsub__op.F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_a(2).T'], o='op_addsub__op_addsub__a(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_a(2).T'], o='op_addsub__op_addsub__a(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__chin_a(2).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__chin_a(2).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__chin_a(0).T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__chin_a(0).T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_a(0).F'], o='op_addsub__op_addsub__a(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_a(0).F'], o='op_addsub__op_addsub__a(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(3).T'], o='op_addsub__op_addsub__b(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(3).T'], o='op_addsub__op_addsub__b(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(3).F'], o='op_addsub__op_addsub__b(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(3).F'], o='op_addsub__op_addsub__b(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(1).T'], o='op_addsub__op_addsub__b(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(1).T'], o='op_addsub__op_addsub__b(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(1).F'], o='op_addsub__op_addsub__b(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(1).F'], o='op_addsub__op_addsub__b(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(2).T'], o='op_addsub__op_addsub__b(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(2).T'], o='op_addsub__op_addsub__b(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__chin_b(2).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__b(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__chin_b(2).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__b(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(3).T'], o='d2__chin_a(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(3).T'], o='d2__chin_a(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(3).F'], o='d2__chin_a(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(3).F'], o='d2__chin_a(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(0).T'], o='d2__chin_b(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(0).T'], o='d2__chin_b(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(0).F'], o='d2__chin_b(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(0).F'], o='d2__chin_b(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(1).T'], o='d2__chin_a(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(1).T'], o='d2__chin_a(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(1).F'], o='d2__chin_a(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(1).F'], o='d2__chin_a(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_op.T'], o='d2__cntrl_select.T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_op.T'], o='d2__cntrl_select.T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_op.F'], o='d2__cntrl_select.F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_op.F'], o='d2__cntrl_select.F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(2).T'], o='d2__chin_a(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(2).T'], o='d2__chin_a(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(2).F'], o='d2__chin_a(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(2).F'], o='d2__chin_a(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(0).T'], o='d2__chin_a(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(0).T'], o='d2__chin_a(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(0).F'], o='d2__chin_a(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(0).F'], o='d2__chin_a(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(3).T'], o='d2__chin_b(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(3).T'], o='d2__chin_b(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(3).F'], o='d2__chin_b(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(3).F'], o='d2__chin_b(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(1).T'], o='d2__chin_b(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(1).T'], o='d2__chin_b(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(1).F'], o='d2__chin_b(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(1).F'], o='d2__chin_b(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(2).T'], o='d2__chin_b(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(2).T'], o='d2__chin_b(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(2).F'], o='d2__chin_b(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(2).F'], o='d2__chin_b(2).F', d=1.0)

	tr.rise(f=tr.NORr, i=['d1__chB_ack', 'd1__chA_ack'], o='b1__en', d=1.0)
	tr.fall(f=tr.NORf, i=['d1__chB_ack', 'd1__chA_ack'], o='b1__en', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(3).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(3).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(3).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(3).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(0).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(0).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(0).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(0).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(1).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(1).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(1).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(1).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(2).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(2).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(2).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(2).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(0).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(0).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(0).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(0).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(3).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(3).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(3).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(3).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(1).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(1).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(1).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(1).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(2).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(2).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(2).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(2).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__cntrl_select.T', 'd2__chin_a(3).T'], o='m__chC_z(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__cntrl_select.T', 'd2__chin_a(3).T'], o='m__chC_z(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(3).F', 'd2__cntrl_select.T'], o='m__chC_z(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(3).F', 'd2__cntrl_select.T'], o='m__chC_z(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(0).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(0).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(0).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(0).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(1).T', 'd2__cntrl_select.T'], o='m__chC_z(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(1).T', 'd2__cntrl_select.T'], o='m__chC_z(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(1).F', 'd2__cntrl_select.T'], o='m__chC_z(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(1).F', 'd2__cntrl_select.T'], o='m__chC_z(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__cntrl_select.T', 'd2__chin_a(2).T'], o='m__chC_z(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__cntrl_select.T', 'd2__chin_a(2).T'], o='m__chC_z(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(2).F', 'd2__cntrl_select.T'], o='m__chC_z(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(2).F', 'd2__cntrl_select.T'], o='m__chC_z(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(0).T', 'd2__cntrl_select.T'], o='m__chC_z(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(0).T', 'd2__cntrl_select.T'], o='m__chC_z(0).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_a(0).F', 'd2__cntrl_select.T'], o='m__chC_z(0).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_a(0).F', 'd2__cntrl_select.T'], o='m__chC_z(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(3).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(3).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(3).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(3).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(3).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(3).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(1).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(1).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(1).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(1).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(1).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(2).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(2).T', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(2).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chin_b(2).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chin_b(2).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(2).F', d=1.0)

	tr.rise(f=tr.ORr, i=['d2__trans1__chin_ack', 'd2__chA_ack'], o='d1__chB_ack', d=1.0)
	tr.fall(f=tr.ORf, i=['d2__trans1__chin_ack', 'd2__chA_ack'], o='d1__chB_ack', d=1.0)

	tr.rise(f=tr.NORr, i=['d2__trans1__chin_b(0).F', 'd2__trans1__chin_b(0).T'], o='d2__trans1__unused_cd_chin_b_0', d=1.0)
	tr.fall(f=tr.NORf, i=['d2__trans1__chin_b(0).F', 'd2__trans1__chin_b(0).T'], o='d2__trans1__unused_cd_chin_b_0', d=1.0)

	tr.rise(f=tr.NORr, i=['d2__trans1__chin_b(3).F', 'd2__trans1__chin_b(3).T'], o='d2__trans1__unused_cd_chin_b_3', d=1.0)
	tr.fall(f=tr.NORf, i=['d2__trans1__chin_b(3).F', 'd2__trans1__chin_b(3).T'], o='d2__trans1__unused_cd_chin_b_3', d=1.0)

	tr.rise(f=tr.NORr, i=['d2__trans1__chin_b(1).F', 'd2__trans1__chin_b(1).T'], o='d2__trans1__unused_cd_chin_b_1', d=1.0)
	tr.fall(f=tr.NORf, i=['d2__trans1__chin_b(1).F', 'd2__trans1__chin_b(1).T'], o='d2__trans1__unused_cd_chin_b_1', d=1.0)

	tr.rise(f=tr.NORr, i=['d2__trans1__chin_b(2).F', 'd2__trans1__chin_b(2).T'], o='d2__trans1__unused_cd_chin_b_2', d=1.0)
	tr.fall(f=tr.NORf, i=['d2__trans1__chin_b(2).F', 'd2__trans1__chin_b(2).T'], o='d2__trans1__unused_cd_chin_b_2', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__trans1__unused_cd_chin_b_3', 'd2__trans1__unused_cd_chin_b_0'], o='d2__trans1__icd_n_lvl0_0', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__trans1__unused_cd_chin_b_3', 'd2__trans1__unused_cd_chin_b_0'], o='d2__trans1__icd_n_lvl0_0', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__trans1__unused_cd_chin_b_2', 'd2__trans1__unused_cd_chin_b_1'], o='d2__trans1__icd_n_lvl0_1', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__trans1__unused_cd_chin_b_2', 'd2__trans1__unused_cd_chin_b_1'], o='d2__trans1__icd_n_lvl0_1', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__trans1__icd_n_lvl0_1', 'd2__trans1__icd_n_lvl0_0'], o='d2__trans1__icd_n', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__trans1__icd_n_lvl0_1', 'd2__trans1__icd_n_lvl0_0'], o='d2__trans1__icd_n', d=1.0)

	tr.rise(f=tr.INVr, i=['d2__trans1__icd_n'], o='d2__trans1__icd', d=1.0)
	tr.fall(f=tr.INVf, i=['d2__trans1__icd_n'], o='d2__trans1__icd', d=1.0)

	tr.rise(f=tr.Cr, i=['d2__chB_ack', 'd2__trans1__icd'], o='d2__trans1__chin_ack', d=1.0)
	tr.fall(f=tr.Cf, i=['d2__chB_ack', 'd2__trans1__icd'], o='d2__trans1__chin_ack', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chA_z(3).F', 'm__chA_z(3).T'], o='m__chA_done', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chA_z(3).F', 'm__chA_z(3).T'], o='m__chA_done', d=1.0)

	tr.rise(f=tr.Cr, i=['m__chout_ack', 'm__chA_done'], o='d1__chA_ack', d=1.0)
	tr.fall(f=tr.Cf, i=['m__chout_ack', 'm__chA_done'], o='d1__chA_ack', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chB_z(2).F', 'm__chB_z(2).T'], o='m__chB_done', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chB_z(2).F', 'm__chB_z(2).T'], o='m__chB_done', d=1.0)

	tr.rise(f=tr.Cr, i=['m__chB_done', 'm__chout_ack'], o='d2__chA_ack', d=1.0)
	tr.fall(f=tr.Cf, i=['m__chB_done', 'm__chout_ack'], o='d2__chA_ack', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chC_z(2).F', 'm__chC_z(2).T'], o='m__chC_done', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chC_z(2).F', 'm__chC_z(2).T'], o='m__chC_done', d=1.0)

	tr.rise(f=tr.Cr, i=['m__chC_done', 'm__chout_ack'], o='d2__chB_ack', d=1.0)
	tr.fall(f=tr.Cf, i=['m__chC_done', 'm__chout_ack'], o='d2__chB_ack', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chB_z(3).T', 'm__chC_z(3).T', 'm__chA_z(3).T'], o='b2__z_in(3).T', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chB_z(3).T', 'm__chC_z(3).T', 'm__chA_z(3).T'], o='b2__z_in(3).T', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chB_z(3).F', 'm__chA_z(3).F', 'm__chC_z(3).F'], o='b2__z_in(3).F', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chB_z(3).F', 'm__chA_z(3).F', 'm__chC_z(3).F'], o='b2__z_in(3).F', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chA_z(1).T', 'm__chC_z(1).T', 'm__chB_z(1).T'], o='b2__z_in(1).T', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chA_z(1).T', 'm__chC_z(1).T', 'm__chB_z(1).T'], o='b2__z_in(1).T', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chA_z(1).F', 'm__chB_z(1).F', 'm__chC_z(1).F'], o='b2__z_in(1).F', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chA_z(1).F', 'm__chB_z(1).F', 'm__chC_z(1).F'], o='b2__z_in(1).F', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chB_z(0).T', 'm__chA_z(0).T', 'm__chC_z(0).T'], o='b2__z_in(0).T', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chB_z(0).T', 'm__chA_z(0).T', 'm__chC_z(0).T'], o='b2__z_in(0).T', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chC_z(0).F', 'm__chA_z(0).F', 'm__chB_z(0).F'], o='b2__z_in(0).F', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chC_z(0).F', 'm__chA_z(0).F', 'm__chB_z(0).F'], o='b2__z_in(0).F', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chA_z(2).T', 'm__chB_z(2).T', 'm__chC_z(2).T'], o='b2__z_in(2).T', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chA_z(2).T', 'm__chB_z(2).T', 'm__chC_z(2).T'], o='b2__z_in(2).T', d=1.0)

	tr.rise(f=tr.ORr, i=['m__chB_z(2).F', 'm__chC_z(2).F', 'm__chA_z(2).F'], o='b2__z_in(2).F', d=1.0)
	tr.fall(f=tr.ORf, i=['m__chB_z(2).F', 'm__chC_z(2).F', 'm__chA_z(2).F'], o='b2__z_in(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(1).T', 'op_or__op_or__a(1).T'], o='op_or__op_or__cell_00__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(1).T', 'op_or__op_or__a(1).T'], o='op_or__op_or__cell_00__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(1).T', 'op_or__op_or__a(1).F'], o='op_or__op_or__cell_00__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(1).T', 'op_or__op_or__a(1).F'], o='op_or__op_or__cell_00__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(1).F', 'op_or__op_or__a(1).T'], o='op_or__op_or__cell_00__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(1).F', 'op_or__op_or__a(1).T'], o='op_or__op_or__cell_00__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(1).F', 'op_or__op_or__b(1).F'], o='m__chB_z(1).F', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(1).F', 'op_or__op_or__b(1).F'], o='m__chB_z(1).F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_or__op_or__cell_00__onehot01', 'op_or__op_or__cell_00__onehot10', 'op_or__op_or__cell_00__onehot00'], o='m__chB_z(1).T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_or__op_or__cell_00__onehot01', 'op_or__op_or__cell_00__onehot10', 'op_or__op_or__cell_00__onehot00'], o='m__chB_z(1).T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(2).T', 'op_or__op_or__b(2).T'], o='op_or__op_or__cell_01__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(2).T', 'op_or__op_or__b(2).T'], o='op_or__op_or__cell_01__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(2).F', 'op_or__op_or__b(2).T'], o='op_or__op_or__cell_01__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(2).F', 'op_or__op_or__b(2).T'], o='op_or__op_or__cell_01__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(2).T', 'op_or__op_or__b(2).F'], o='op_or__op_or__cell_01__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(2).T', 'op_or__op_or__b(2).F'], o='op_or__op_or__cell_01__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(2).F', 'op_or__op_or__b(2).F'], o='m__chB_z(2).F', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(2).F', 'op_or__op_or__b(2).F'], o='m__chB_z(2).F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_or__op_or__cell_01__onehot01', 'op_or__op_or__cell_01__onehot10', 'op_or__op_or__cell_01__onehot00'], o='m__chB_z(2).T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_or__op_or__cell_01__onehot01', 'op_or__op_or__cell_01__onehot10', 'op_or__op_or__cell_01__onehot00'], o='m__chB_z(2).T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(3).T', 'op_or__op_or__a(3).T'], o='op_or__op_or__cell_02__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(3).T', 'op_or__op_or__a(3).T'], o='op_or__op_or__cell_02__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(3).T', 'op_or__op_or__a(3).F'], o='op_or__op_or__cell_02__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(3).T', 'op_or__op_or__a(3).F'], o='op_or__op_or__cell_02__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(3).T', 'op_or__op_or__b(3).F'], o='op_or__op_or__cell_02__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(3).T', 'op_or__op_or__b(3).F'], o='op_or__op_or__cell_02__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(3).F', 'op_or__op_or__b(3).F'], o='m__chB_z(3).F', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(3).F', 'op_or__op_or__b(3).F'], o='m__chB_z(3).F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_or__op_or__cell_02__onehot00', 'op_or__op_or__cell_02__onehot01', 'op_or__op_or__cell_02__onehot10'], o='m__chB_z(3).T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_or__op_or__cell_02__onehot00', 'op_or__op_or__cell_02__onehot01', 'op_or__op_or__cell_02__onehot10'], o='m__chB_z(3).T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(0).T', 'op_or__op_or__b(0).T'], o='op_or__op_or__cell_03__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(0).T', 'op_or__op_or__b(0).T'], o='op_or__op_or__cell_03__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(0).T', 'op_or__op_or__a(0).F'], o='op_or__op_or__cell_03__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(0).T', 'op_or__op_or__a(0).F'], o='op_or__op_or__cell_03__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(0).T', 'op_or__op_or__b(0).F'], o='op_or__op_or__cell_03__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(0).T', 'op_or__op_or__b(0).F'], o='op_or__op_or__cell_03__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(0).F', 'op_or__op_or__b(0).F'], o='m__chB_z(0).F', d=1.0)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(0).F', 'op_or__op_or__b(0).F'], o='m__chB_z(0).F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_or__op_or__cell_03__onehot00', 'op_or__op_or__cell_03__onehot10', 'op_or__op_or__cell_03__onehot01'], o='m__chB_z(0).T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_or__op_or__cell_03__onehot00', 'op_or__op_or__cell_03__onehot10', 'op_or__op_or__cell_03__onehot01'], o='m__chB_z(0).T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__a(0).F'], o='op_addsub__op_addsub__cell_23__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__a(0).F'], o='op_addsub__op_addsub__cell_23__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__a(0).T'], o='op_addsub__op_addsub__cell_23__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__a(0).T'], o='op_addsub__op_addsub__cell_23__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__a(0).F'], o='op_addsub__op_addsub__cell_23__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__a(0).F'], o='op_addsub__op_addsub__cell_23__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__a(0).T'], o='op_addsub__op_addsub__cell_23__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__a(0).T'], o='op_addsub__op_addsub__cell_23__onehot11', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_23__onehot10', 'op_addsub__op_addsub__cell_23__onehot01', 'op_addsub__op_addsub__cell_23__onehot00'], o='op_addsub__op_addsub__cell_10__a_F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_23__onehot10', 'op_addsub__op_addsub__cell_23__onehot01', 'op_addsub__op_addsub__cell_23__onehot00'], o='op_addsub__op_addsub__cell_10__a_F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_18__b.T', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_18__b.T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_02__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_02__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_02__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_02__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_02__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_02__onehot00', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_18__b.T', 'op_addsub__op_addsub__cell_02__onehot10', 'op_addsub__op_addsub__cell_02__onehot01'], o='op_addsub__op_addsub__cell_04__a_T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_18__b.T', 'op_addsub__op_addsub__cell_02__onehot10', 'op_addsub__op_addsub__cell_02__onehot01'], o='op_addsub__op_addsub__cell_04__a_T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_02__onehot00', 'op_addsub__op_addsub__cell_02__onehot10', 'op_addsub__op_addsub__cell_02__onehot01'], o='op_addsub__op_addsub__cell_18__b.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_02__onehot00', 'op_addsub__op_addsub__cell_02__onehot10', 'op_addsub__op_addsub__cell_02__onehot01'], o='op_addsub__op_addsub__cell_18__b.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_03__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_03__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_18__b.F'], o='op_addsub__op_addsub__cell_03__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_18__b.F'], o='op_addsub__op_addsub__cell_03__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_03__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_03__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_18__b.F', 'op_addsub__op_addsub__op.F'], o='op_addsub__op_addsub__cell_12__b.T', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_18__b.F', 'op_addsub__op_addsub__op.F'], o='op_addsub__op_addsub__cell_12__b.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_03__onehot01', 'op_addsub__op_addsub__cell_03__onehot00', 'op_addsub__op_addsub__cell_03__onehot10'], o='op_addsub__op_addsub__cell_12__b.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_03__onehot01', 'op_addsub__op_addsub__cell_03__onehot00', 'op_addsub__op_addsub__cell_03__onehot10'], o='op_addsub__op_addsub__cell_12__b.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__cell_02__onehot00'], o='op_addsub__op_addsub__cell_04__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__cell_02__onehot00'], o='op_addsub__op_addsub__cell_04__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__cell_02__onehot00'], o='op_addsub__op_addsub__cell_04__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__cell_02__onehot00'], o='op_addsub__op_addsub__cell_04__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__cell_04__a_T'], o='op_addsub__op_addsub__cell_04__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__cell_04__a_T'], o='op_addsub__op_addsub__cell_04__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__cell_04__a_T'], o='op_addsub__op_addsub__cell_06__a.F', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__cell_04__a_T'], o='op_addsub__op_addsub__cell_06__a.F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_04__onehot00', 'op_addsub__op_addsub__cell_04__onehot10', 'op_addsub__op_addsub__cell_04__onehot01'], o='op_addsub__op_addsub__cell_06__a.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_04__onehot00', 'op_addsub__op_addsub__cell_04__onehot10', 'op_addsub__op_addsub__cell_04__onehot01'], o='op_addsub__op_addsub__cell_06__a.T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_05__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_05__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_05__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_05__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_05__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_05__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_06__b.F', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_06__b.F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_05__onehot10', 'op_addsub__op_addsub__cell_05__onehot00', 'op_addsub__op_addsub__cell_05__onehot01'], o='op_addsub__op_addsub__cell_06__b.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_05__onehot10', 'op_addsub__op_addsub__cell_05__onehot00', 'op_addsub__op_addsub__cell_05__onehot01'], o='op_addsub__op_addsub__cell_06__b.T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_06__a.F', 'op_addsub__op_addsub__cell_06__b.F'], o='op_addsub__op_addsub__cell_06__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_06__a.F', 'op_addsub__op_addsub__cell_06__b.F'], o='op_addsub__op_addsub__cell_06__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_06__b.T', 'op_addsub__op_addsub__cell_06__a.F'], o='op_addsub__op_addsub__cell_06__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_06__b.T', 'op_addsub__op_addsub__cell_06__a.F'], o='op_addsub__op_addsub__cell_06__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_06__b.F', 'op_addsub__op_addsub__cell_06__a.T'], o='op_addsub__op_addsub__cell_06__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_06__b.F', 'op_addsub__op_addsub__cell_06__a.T'], o='op_addsub__op_addsub__cell_06__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_06__b.T', 'op_addsub__op_addsub__cell_06__a.T'], o='op_addsub__op_addsub__cell_08__b.T', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_06__b.T', 'op_addsub__op_addsub__cell_06__a.T'], o='op_addsub__op_addsub__cell_08__b.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_06__onehot01', 'op_addsub__op_addsub__cell_06__onehot10', 'op_addsub__op_addsub__cell_06__onehot00'], o='op_addsub__op_addsub__cell_08__b.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_06__onehot01', 'op_addsub__op_addsub__cell_06__onehot10', 'op_addsub__op_addsub__cell_06__onehot00'], o='op_addsub__op_addsub__cell_08__b.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__a(1).F', 'op_addsub__op_addsub__cell_08__b.T'], o='op_addsub__op_addsub__cell_08__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__a(1).F', 'op_addsub__op_addsub__cell_08__b.T'], o='op_addsub__op_addsub__cell_08__onehot11', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_08__b.F', 'op_addsub__op_addsub__a(1).F'], o='op_addsub__op_addsub__cell_08__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_08__b.F', 'op_addsub__op_addsub__a(1).F'], o='op_addsub__op_addsub__cell_08__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__a(1).T', 'op_addsub__op_addsub__cell_08__b.T'], o='op_addsub__op_addsub__cell_08__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__a(1).T', 'op_addsub__op_addsub__cell_08__b.T'], o='op_addsub__op_addsub__cell_08__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__a(1).T', 'op_addsub__op_addsub__cell_08__b.F'], o='op_addsub__op_addsub__cell_08__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__a(1).T', 'op_addsub__op_addsub__cell_08__b.F'], o='op_addsub__op_addsub__cell_08__onehot00', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_08__onehot01', 'op_addsub__op_addsub__cell_08__onehot11', 'op_addsub__op_addsub__cell_08__onehot10'], o='op_addsub__op_addsub__cell_11__a_T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_08__onehot01', 'op_addsub__op_addsub__cell_08__onehot11', 'op_addsub__op_addsub__cell_08__onehot10'], o='op_addsub__op_addsub__cell_11__a_T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_08__onehot01', 'op_addsub__op_addsub__cell_08__onehot10'], o='op_addsub__op_addsub__cell_10__b.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_08__onehot01', 'op_addsub__op_addsub__cell_08__onehot10'], o='op_addsub__op_addsub__cell_10__b.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_08__onehot11'], o='op_addsub__op_addsub__cell_10__b.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_08__onehot11'], o='op_addsub__op_addsub__cell_10__b.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_10__a_F', 'op_addsub__op_addsub__cell_10__b.F'], o='op_addsub__op_addsub__cell_10__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_10__a_F', 'op_addsub__op_addsub__cell_10__b.F'], o='op_addsub__op_addsub__cell_10__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_10__b.T', 'op_addsub__op_addsub__cell_10__a_F'], o='op_addsub__op_addsub__cell_10__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_10__b.T', 'op_addsub__op_addsub__cell_10__a_F'], o='op_addsub__op_addsub__cell_10__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_10__b.F'], o='op_addsub__op_addsub__cell_10__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_10__b.F'], o='op_addsub__op_addsub__cell_10__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_10__b.T'], o='op_addsub__op_addsub__cell_10__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_10__b.T'], o='op_addsub__op_addsub__cell_10__onehot11', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_10__onehot00', 'op_addsub__op_addsub__cell_10__onehot01', 'op_addsub__op_addsub__cell_10__onehot10'], o='op_addsub__op_addsub__cell_11__b_T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_10__onehot00', 'op_addsub__op_addsub__cell_10__onehot01', 'op_addsub__op_addsub__cell_10__onehot10'], o='op_addsub__op_addsub__cell_11__b_T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_10__onehot01', 'op_addsub__op_addsub__cell_10__onehot10'], o='m__chA_z(1).T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_10__onehot01', 'op_addsub__op_addsub__cell_10__onehot10'], o='m__chA_z(1).T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_10__onehot00', 'op_addsub__op_addsub__cell_10__onehot11'], o='m__chA_z(1).F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_10__onehot00', 'op_addsub__op_addsub__cell_10__onehot11'], o='m__chA_z(1).F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_10__onehot11'], o='op_addsub__op_addsub__cell_11__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_10__onehot11'], o='op_addsub__op_addsub__cell_11__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_11__b_T'], o='op_addsub__op_addsub__cell_11__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_11__b_T'], o='op_addsub__op_addsub__cell_11__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_10__onehot11', 'op_addsub__op_addsub__cell_11__a_T'], o='op_addsub__op_addsub__cell_11__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_10__onehot11', 'op_addsub__op_addsub__cell_11__a_T'], o='op_addsub__op_addsub__cell_11__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_11__a_T', 'op_addsub__op_addsub__cell_11__b_T'], o='op_addsub__op_addsub__cell_16__a.F', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_11__a_T', 'op_addsub__op_addsub__cell_11__b_T'], o='op_addsub__op_addsub__cell_16__a.F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_11__onehot00', 'op_addsub__op_addsub__cell_11__onehot10', 'op_addsub__op_addsub__cell_11__onehot01'], o='op_addsub__op_addsub__cell_16__a.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_11__onehot00', 'op_addsub__op_addsub__cell_11__onehot10', 'op_addsub__op_addsub__cell_11__onehot01'], o='op_addsub__op_addsub__cell_16__a.T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_12__b.F'], o='op_addsub__op_addsub__cell_12__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_12__b.F'], o='op_addsub__op_addsub__cell_12__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_12__b.T'], o='op_addsub__op_addsub__cell_12__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_12__b.T'], o='op_addsub__op_addsub__cell_12__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_12__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_12__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_12__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_12__onehot11', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_12__onehot01', 'op_addsub__op_addsub__cell_12__onehot10'], o='op_addsub__op_addsub__cell_14__b.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_12__onehot01', 'op_addsub__op_addsub__cell_12__onehot10'], o='op_addsub__op_addsub__cell_14__b.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_12__onehot11', 'op_addsub__op_addsub__cell_12__onehot00'], o='op_addsub__op_addsub__cell_14__b.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_12__onehot11', 'op_addsub__op_addsub__cell_12__onehot00'], o='op_addsub__op_addsub__cell_14__b.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_14__b.F', 'op_addsub__op_addsub__a(2).F'], o='op_addsub__op_addsub__cell_14__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_14__b.F', 'op_addsub__op_addsub__a(2).F'], o='op_addsub__op_addsub__cell_14__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_14__b.T', 'op_addsub__op_addsub__a(2).F'], o='op_addsub__op_addsub__cell_14__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_14__b.T', 'op_addsub__op_addsub__a(2).F'], o='op_addsub__op_addsub__cell_14__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_14__b.F', 'op_addsub__op_addsub__a(2).T'], o='op_addsub__op_addsub__cell_14__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_14__b.F', 'op_addsub__op_addsub__a(2).T'], o='op_addsub__op_addsub__cell_14__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_14__b.T', 'op_addsub__op_addsub__a(2).T'], o='op_addsub__op_addsub__cell_14__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_14__b.T', 'op_addsub__op_addsub__a(2).T'], o='op_addsub__op_addsub__cell_14__onehot11', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_14__onehot10', 'op_addsub__op_addsub__cell_14__onehot01', 'op_addsub__op_addsub__cell_14__onehot00'], o='op_addsub__op_addsub__cell_17__a_T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_14__onehot10', 'op_addsub__op_addsub__cell_14__onehot01', 'op_addsub__op_addsub__cell_14__onehot00'], o='op_addsub__op_addsub__cell_17__a_T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_14__onehot10', 'op_addsub__op_addsub__cell_14__onehot01'], o='op_addsub__op_addsub__cell_16__b.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_14__onehot10', 'op_addsub__op_addsub__cell_14__onehot01'], o='op_addsub__op_addsub__cell_16__b.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_14__onehot00', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_16__b.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_14__onehot00', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_16__b.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__a.F', 'op_addsub__op_addsub__cell_16__b.F'], o='op_addsub__op_addsub__cell_16__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__a.F', 'op_addsub__op_addsub__cell_16__b.F'], o='op_addsub__op_addsub__cell_16__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__a.F', 'op_addsub__op_addsub__cell_16__b.T'], o='op_addsub__op_addsub__cell_16__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__a.F', 'op_addsub__op_addsub__cell_16__b.T'], o='op_addsub__op_addsub__cell_16__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__b.F', 'op_addsub__op_addsub__cell_16__a.T'], o='op_addsub__op_addsub__cell_16__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__b.F', 'op_addsub__op_addsub__cell_16__a.T'], o='op_addsub__op_addsub__cell_16__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__a.T', 'op_addsub__op_addsub__cell_16__b.T'], o='op_addsub__op_addsub__cell_16__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__a.T', 'op_addsub__op_addsub__cell_16__b.T'], o='op_addsub__op_addsub__cell_16__onehot11', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_16__onehot01', 'op_addsub__op_addsub__cell_16__onehot00', 'op_addsub__op_addsub__cell_16__onehot10'], o='op_addsub__op_addsub__cell_17__b_T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_16__onehot01', 'op_addsub__op_addsub__cell_16__onehot00', 'op_addsub__op_addsub__cell_16__onehot10'], o='op_addsub__op_addsub__cell_17__b_T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_16__onehot01', 'op_addsub__op_addsub__cell_16__onehot10'], o='m__chA_z(2).T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_16__onehot01', 'op_addsub__op_addsub__cell_16__onehot10'], o='m__chA_z(2).T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_16__onehot00'], o='m__chA_z(2).F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_16__onehot00'], o='m__chA_z(2).F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_17__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_17__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_17__b_T', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_17__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_17__b_T', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_17__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_17__a_T'], o='op_addsub__op_addsub__cell_17__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_17__a_T'], o='op_addsub__op_addsub__cell_17__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_17__a_T', 'op_addsub__op_addsub__cell_17__b_T'], o='op_addsub__op_addsub__cell_22__a.T', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_17__a_T', 'op_addsub__op_addsub__cell_17__b_T'], o='op_addsub__op_addsub__cell_22__a.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_17__onehot10', 'op_addsub__op_addsub__cell_17__onehot00', 'op_addsub__op_addsub__cell_17__onehot01'], o='op_addsub__op_addsub__cell_22__a.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_17__onehot10', 'op_addsub__op_addsub__cell_17__onehot00', 'op_addsub__op_addsub__cell_17__onehot01'], o='op_addsub__op_addsub__cell_22__a.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_18__b.F', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_18__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_18__b.F', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_18__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_18__b.T', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_18__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_18__b.T', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_18__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_18__b.F'], o='op_addsub__op_addsub__cell_18__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_18__b.F'], o='op_addsub__op_addsub__cell_18__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_19__b.F', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_19__b.F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_18__onehot01', 'op_addsub__op_addsub__cell_18__onehot10', 'op_addsub__op_addsub__cell_18__onehot00'], o='op_addsub__op_addsub__cell_19__b.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_18__onehot01', 'op_addsub__op_addsub__cell_18__onehot10', 'op_addsub__op_addsub__cell_18__onehot00'], o='op_addsub__op_addsub__cell_19__b.T', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_19__b.F'], o='op_addsub__op_addsub__cell_19__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_19__b.F'], o='op_addsub__op_addsub__cell_19__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_19__b.T'], o='op_addsub__op_addsub__cell_19__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_19__b.T'], o='op_addsub__op_addsub__cell_19__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__cell_19__b.F'], o='op_addsub__op_addsub__cell_19__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__cell_19__b.F'], o='op_addsub__op_addsub__cell_19__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_19__b.T', 'op_addsub__op_addsub__op.F'], o='op_addsub__op_addsub__cell_21__a.T', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_19__b.T', 'op_addsub__op_addsub__op.F'], o='op_addsub__op_addsub__cell_21__a.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_19__onehot10', 'op_addsub__op_addsub__cell_19__onehot00', 'op_addsub__op_addsub__cell_19__onehot01'], o='op_addsub__op_addsub__cell_21__a.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_19__onehot10', 'op_addsub__op_addsub__cell_19__onehot00', 'op_addsub__op_addsub__cell_19__onehot01'], o='op_addsub__op_addsub__cell_21__a.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(3).T', 'op_addsub__op_addsub__a(3).F'], o='op_addsub__op_addsub__cell_20__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(3).T', 'op_addsub__op_addsub__a(3).F'], o='op_addsub__op_addsub__cell_20__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(3).T', 'op_addsub__op_addsub__a(3).T'], o='op_addsub__op_addsub__cell_20__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(3).T', 'op_addsub__op_addsub__a(3).T'], o='op_addsub__op_addsub__cell_20__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(3).F', 'op_addsub__op_addsub__a(3).F'], o='op_addsub__op_addsub__cell_20__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(3).F', 'op_addsub__op_addsub__a(3).F'], o='op_addsub__op_addsub__cell_20__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(3).F', 'op_addsub__op_addsub__a(3).T'], o='op_addsub__op_addsub__cell_20__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(3).F', 'op_addsub__op_addsub__a(3).T'], o='op_addsub__op_addsub__cell_20__onehot11', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_20__onehot01', 'op_addsub__op_addsub__cell_20__onehot10'], o='op_addsub__op_addsub__cell_21__b.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_20__onehot01', 'op_addsub__op_addsub__cell_20__onehot10'], o='op_addsub__op_addsub__cell_21__b.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_20__onehot11', 'op_addsub__op_addsub__cell_20__onehot00'], o='op_addsub__op_addsub__cell_21__b.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_20__onehot11', 'op_addsub__op_addsub__cell_20__onehot00'], o='op_addsub__op_addsub__cell_21__b.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_21__b.F', 'op_addsub__op_addsub__cell_21__a.F'], o='op_addsub__op_addsub__cell_21__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_21__b.F', 'op_addsub__op_addsub__cell_21__a.F'], o='op_addsub__op_addsub__cell_21__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_21__b.T', 'op_addsub__op_addsub__cell_21__a.F'], o='op_addsub__op_addsub__cell_21__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_21__b.T', 'op_addsub__op_addsub__cell_21__a.F'], o='op_addsub__op_addsub__cell_21__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_21__b.F', 'op_addsub__op_addsub__cell_21__a.T'], o='op_addsub__op_addsub__cell_21__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_21__b.F', 'op_addsub__op_addsub__cell_21__a.T'], o='op_addsub__op_addsub__cell_21__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_21__b.T', 'op_addsub__op_addsub__cell_21__a.T'], o='op_addsub__op_addsub__cell_21__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_21__b.T', 'op_addsub__op_addsub__cell_21__a.T'], o='op_addsub__op_addsub__cell_21__onehot11', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_21__onehot01', 'op_addsub__op_addsub__cell_21__onehot10'], o='op_addsub__op_addsub__cell_22__b.T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_21__onehot01', 'op_addsub__op_addsub__cell_21__onehot10'], o='op_addsub__op_addsub__cell_22__b.T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_21__onehot00', 'op_addsub__op_addsub__cell_21__onehot11'], o='op_addsub__op_addsub__cell_22__b.F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_21__onehot00', 'op_addsub__op_addsub__cell_21__onehot11'], o='op_addsub__op_addsub__cell_22__b.F', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_22__b.F', 'op_addsub__op_addsub__cell_22__a.F'], o='op_addsub__op_addsub__cell_22__onehot00', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_22__b.F', 'op_addsub__op_addsub__cell_22__a.F'], o='op_addsub__op_addsub__cell_22__onehot00', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_22__a.F', 'op_addsub__op_addsub__cell_22__b.T'], o='op_addsub__op_addsub__cell_22__onehot01', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_22__a.F', 'op_addsub__op_addsub__cell_22__b.T'], o='op_addsub__op_addsub__cell_22__onehot01', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_22__b.F', 'op_addsub__op_addsub__cell_22__a.T'], o='op_addsub__op_addsub__cell_22__onehot10', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_22__b.F', 'op_addsub__op_addsub__cell_22__a.T'], o='op_addsub__op_addsub__cell_22__onehot10', d=1.0)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_22__b.T', 'op_addsub__op_addsub__cell_22__a.T'], o='op_addsub__op_addsub__cell_22__onehot11', d=1.0)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_22__b.T', 'op_addsub__op_addsub__cell_22__a.T'], o='op_addsub__op_addsub__cell_22__onehot11', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_22__onehot10', 'op_addsub__op_addsub__cell_22__onehot01'], o='m__chA_z(3).T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_22__onehot10', 'op_addsub__op_addsub__cell_22__onehot01'], o='m__chA_z(3).T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_22__onehot00', 'op_addsub__op_addsub__cell_22__onehot11'], o='m__chA_z(3).F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_22__onehot00', 'op_addsub__op_addsub__cell_22__onehot11'], o='m__chA_z(3).F', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_23__onehot10', 'op_addsub__op_addsub__cell_23__onehot01'], o='m__chA_z(0).T', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_23__onehot10', 'op_addsub__op_addsub__cell_23__onehot01'], o='m__chA_z(0).T', d=1.0)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_23__onehot00'], o='m__chA_z(0).F', d=1.0)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_23__onehot00'], o='m__chA_z(0).F', d=1.0)

	# input_signals = {b(1).F, a(3).F, op(0).T, op(1).F, op(1).T, b(0).F, b(1).T, reset, b(2).T, a(3).T, a(1).F, a(1).T, a(0).F, a(2).F, b(3).T, op(0).F, a(0).T, b(2).F, ack_in, a(2).T, b(3).F, b(0).T}

	init = {
	'op(0).T' : 0,
	'op(0).F' : 0,
	'op(1).T' : 0,
	'op(1).F' : 0,
	'a(0).T' : 0,
	'a(3).F' : 0,
	'a(2).T' : 0,
	'a(0).F' : 0,
	'a(3).T' : 0,
	'a(1).T' : 0,
	'a(1).F' : 0,
	'a(2).F' : 0,
	'b(1).F' : 0,
	'b(3).T' : 0,
	'b(0).F' : 0,
	'b(2).F' : 0,
	'b(1).T' : 0,
	'b(2).T' : 0,
	'b(3).F' : 0,
	'b(0).T' : 0,
	'ack_in' : 0,
	'z(3).F' : 0,
	'z(1).T' : 0,
	'z(2).T' : 0,
	'z(2).F' : 0,
	'z(3).T' : 0,
	'z(1).F' : 0,
	'z(0).F' : 0,
	'z(0).T' : 0,
	'd1__chin_op.T' : 0,
	'd1__chin_op.F' : 0,
	'd1__cntrl_select.T' : 0,
	'd1__cntrl_select.F' : 0,
	'd1__chin_a(0).T' : 0,
	'd1__chin_a(0).F' : 0,
	'd1__chin_a(1).T' : 0,
	'd1__chin_a(1).F' : 0,
	'd1__chin_a(2).F' : 0,
	'd1__chin_a(2).T' : 0,
	'd1__chin_a(3).F' : 0,
	'd1__chin_a(3).T' : 0,
	'd1__chin_b(0).T' : 0,
	'd1__chin_b(0).F' : 0,
	'd1__chin_b(1).T' : 0,
	'd1__chin_b(1).F' : 0,
	'd1__chin_b(2).F' : 0,
	'd1__chin_b(2).T' : 0,
	'd1__chin_b(3).F' : 0,
	'd1__chin_b(3).T' : 0,
	'b2__c_z_out_0' : 1,
	'b2__en' : 1,
	'b2__c_z_out_1' : 1,
	'b2__c_z_out_2' : 1,
	'b2__c_z_out_3' : 1,
	'b2__ocd_n_lvl0_0' : 1,
	'b2__ocd_n_lvl0_1' : 1,
	'b2__ocd_n' : 1,
	'm__chout_ack' : 0,
	'op_addsub__op_addsub__a(3).T' : 0,
	'op_addsub__op_addsub__a(3).F' : 0,
	'op_addsub__op_addsub__b(0).T' : 0,
	'op_addsub__op_addsub__b(0).F' : 0,
	'op_addsub__op_addsub__a(1).T' : 0,
	'op_addsub__op_addsub__a(1).F' : 0,
	'op_addsub__op_addsub__op.T' : 0,
	'op_addsub__op_addsub__op.F' : 0,
	'op_addsub__op_addsub__a(2).T' : 0,
	'op_addsub__op_addsub__a(2).F' : 0,
	'op_addsub__op_addsub__a(0).T' : 0,
	'op_addsub__op_addsub__a(0).F' : 0,
	'op_addsub__op_addsub__b(3).T' : 0,
	'op_addsub__op_addsub__b(3).F' : 0,
	'op_addsub__op_addsub__b(1).T' : 0,
	'op_addsub__op_addsub__b(1).F' : 0,
	'op_addsub__op_addsub__b(2).T' : 0,
	'op_addsub__op_addsub__b(2).F' : 0,
	'd2__chin_a(3).T' : 0,
	'd2__chin_a(3).F' : 0,
	'd2__chin_b(0).T' : 0,
	'd2__chin_b(0).F' : 0,
	'd2__chin_a(1).T' : 0,
	'd2__chin_a(1).F' : 0,
	'd2__cntrl_select.T' : 0,
	'd2__cntrl_select.F' : 0,
	'd2__chin_a(2).T' : 0,
	'd2__chin_a(2).F' : 0,
	'd2__chin_a(0).T' : 0,
	'd2__chin_a(0).F' : 0,
	'd2__chin_b(3).T' : 0,
	'd2__chin_b(3).F' : 0,
	'd2__chin_b(1).T' : 0,
	'd2__chin_b(1).F' : 0,
	'd2__chin_b(2).T' : 0,
	'd2__chin_b(2).F' : 0,
	'op_or__op_or__a(3).T' : 0,
	'op_or__op_or__a(3).F' : 0,
	'op_or__op_or__b(0).T' : 0,
	'op_or__op_or__b(0).F' : 0,
	'op_or__op_or__a(1).T' : 0,
	'op_or__op_or__a(1).F' : 0,
	'op_or__op_or__a(2).T' : 0,
	'op_or__op_or__a(2).F' : 0,
	'op_or__op_or__a(0).T' : 0,
	'op_or__op_or__a(0).F' : 0,
	'op_or__op_or__b(3).T' : 0,
	'op_or__op_or__b(3).F' : 0,
	'op_or__op_or__b(1).T' : 0,
	'op_or__op_or__b(1).F' : 0,
	'op_or__op_or__b(2).T' : 0,
	'op_or__op_or__b(2).F' : 0,
	'm__chC_z(3).F' : 0,
	'm__chC_z(3).T' : 0,
	'd2__trans1__chin_b(0).T' : 0,
	'd2__trans1__chin_b(0).F' : 0,
	'm__chC_z(1).F' : 0,
	'm__chC_z(1).T' : 0,
	'm__chC_z(2).F' : 0,
	'm__chC_z(2).T' : 0,
	'm__chC_z(0).F' : 0,
	'm__chC_z(0).T' : 0,
	'd2__trans1__chin_b(3).T' : 0,
	'd2__trans1__chin_b(3).F' : 0,
	'd2__trans1__chin_b(1).T' : 0,
	'd2__trans1__chin_b(1).F' : 0,
	'd2__trans1__chin_b(2).T' : 0,
	'd2__trans1__chin_b(2).F' : 0,
	'd2__trans1__unused_cd_chin_b_0' : 1,
	'd2__trans1__unused_cd_chin_b_3' : 1,
	'd2__trans1__unused_cd_chin_b_1' : 1,
	'd2__trans1__unused_cd_chin_b_2' : 1,
	'd2__trans1__icd_n_lvl0_0' : 1,
	'd2__trans1__icd_n_lvl0_1' : 1,
	'd2__trans1__icd_n' : 1,
	'd2__trans1__icd' : 0,
	'm__chB_z(2).F' : 0,
	'm__chC_done' : 0,
	'm__chB_z(3).F' : 0,
	'm__chB_z(1).F' : 0,
	'm__chB_z(0).F' : 0,
	'op_or__op_or__cell_00__onehot00' : 0,
	'op_or__op_or__cell_00__onehot01' : 0,
	'op_or__op_or__cell_00__onehot10' : 0,
	'op_or__op_or__cell_01__onehot00' : 0,
	'op_or__op_or__cell_01__onehot01' : 0,
	'op_or__op_or__cell_01__onehot10' : 0,
	'op_or__op_or__cell_02__onehot00' : 0,
	'op_or__op_or__cell_02__onehot01' : 0,
	'op_or__op_or__cell_02__onehot10' : 0,
	'op_or__op_or__cell_03__onehot00' : 0,
	'op_or__op_or__cell_03__onehot01' : 0,
	'op_or__op_or__cell_03__onehot10' : 0,
	'op_addsub__op_addsub__cell_23__onehot00' : 0,
	'op_addsub__op_addsub__cell_23__onehot01' : 0,
	'op_addsub__op_addsub__cell_23__onehot10' : 0,
	'op_addsub__op_addsub__cell_23__onehot11' : 0,
	'op_addsub__op_addsub__cell_10__a_F' : 0,
	'op_addsub__op_addsub__cell_18__b.T' : 0,
	'op_addsub__op_addsub__cell_02__onehot10' : 0,
	'op_addsub__op_addsub__cell_02__onehot01' : 0,
	'op_addsub__op_addsub__cell_02__onehot00' : 0,
	'op_addsub__op_addsub__cell_04__a_T' : 0,
	'op_addsub__op_addsub__cell_18__b.F' : 0,
	'op_addsub__op_addsub__cell_03__onehot00' : 0,
	'op_addsub__op_addsub__cell_03__onehot01' : 0,
	'op_addsub__op_addsub__cell_03__onehot10' : 0,
	'op_addsub__op_addsub__cell_12__b.T' : 0,
	'op_addsub__op_addsub__cell_12__b.F' : 0,
	'op_addsub__op_addsub__cell_04__onehot00' : 0,
	'op_addsub__op_addsub__cell_04__onehot01' : 0,
	'op_addsub__op_addsub__cell_04__onehot10' : 0,
	'op_addsub__op_addsub__cell_06__a.F' : 0,
	'op_addsub__op_addsub__cell_06__a.T' : 0,
	'op_addsub__op_addsub__cell_05__onehot00' : 0,
	'op_addsub__op_addsub__cell_05__onehot01' : 0,
	'op_addsub__op_addsub__cell_05__onehot10' : 0,
	'op_addsub__op_addsub__cell_06__b.F' : 0,
	'op_addsub__op_addsub__cell_06__b.T' : 0,
	'op_addsub__op_addsub__cell_06__onehot00' : 0,
	'op_addsub__op_addsub__cell_06__onehot01' : 0,
	'op_addsub__op_addsub__cell_06__onehot10' : 0,
	'op_addsub__op_addsub__cell_08__b.T' : 0,
	'op_addsub__op_addsub__cell_08__b.F' : 0,
	'op_addsub__op_addsub__cell_08__onehot11' : 0,
	'op_addsub__op_addsub__cell_08__onehot10' : 0,
	'op_addsub__op_addsub__cell_08__onehot01' : 0,
	'op_addsub__op_addsub__cell_08__onehot00' : 0,
	'op_addsub__op_addsub__cell_11__a_T' : 0,
	'op_addsub__op_addsub__cell_10__b.T' : 0,
	'op_addsub__op_addsub__cell_10__b.F' : 0,
	'op_addsub__op_addsub__cell_10__onehot00' : 0,
	'op_addsub__op_addsub__cell_10__onehot01' : 0,
	'op_addsub__op_addsub__cell_10__onehot10' : 0,
	'op_addsub__op_addsub__cell_10__onehot11' : 0,
	'op_addsub__op_addsub__cell_11__b_T' : 0,
	'op_addsub__op_addsub__cell_11__onehot00' : 0,
	'op_addsub__op_addsub__cell_11__onehot01' : 0,
	'op_addsub__op_addsub__cell_11__onehot10' : 0,
	'op_addsub__op_addsub__cell_16__a.F' : 0,
	'op_addsub__op_addsub__cell_16__a.T' : 0,
	'op_addsub__op_addsub__cell_12__onehot00' : 0,
	'op_addsub__op_addsub__cell_12__onehot01' : 0,
	'op_addsub__op_addsub__cell_12__onehot10' : 0,
	'op_addsub__op_addsub__cell_12__onehot11' : 0,
	'op_addsub__op_addsub__cell_14__b.T' : 0,
	'op_addsub__op_addsub__cell_14__b.F' : 0,
	'op_addsub__op_addsub__cell_14__onehot00' : 0,
	'op_addsub__op_addsub__cell_14__onehot01' : 0,
	'op_addsub__op_addsub__cell_14__onehot10' : 0,
	'op_addsub__op_addsub__cell_14__onehot11' : 0,
	'op_addsub__op_addsub__cell_17__a_T' : 0,
	'op_addsub__op_addsub__cell_16__b.T' : 0,
	'op_addsub__op_addsub__cell_16__b.F' : 0,
	'op_addsub__op_addsub__cell_16__onehot00' : 0,
	'op_addsub__op_addsub__cell_16__onehot01' : 0,
	'op_addsub__op_addsub__cell_16__onehot10' : 0,
	'op_addsub__op_addsub__cell_16__onehot11' : 0,
	'op_addsub__op_addsub__cell_17__b_T' : 0,
	'op_addsub__op_addsub__cell_17__onehot00' : 0,
	'op_addsub__op_addsub__cell_17__onehot01' : 0,
	'op_addsub__op_addsub__cell_17__onehot10' : 0,
	'op_addsub__op_addsub__cell_22__a.T' : 0,
	'op_addsub__op_addsub__cell_22__a.F' : 0,
	'op_addsub__op_addsub__cell_18__onehot00' : 0,
	'op_addsub__op_addsub__cell_18__onehot01' : 0,
	'op_addsub__op_addsub__cell_18__onehot10' : 0,
	'op_addsub__op_addsub__cell_19__b.F' : 0,
	'op_addsub__op_addsub__cell_19__b.T' : 0,
	'op_addsub__op_addsub__cell_19__onehot00' : 0,
	'op_addsub__op_addsub__cell_19__onehot01' : 0,
	'op_addsub__op_addsub__cell_19__onehot10' : 0,
	'op_addsub__op_addsub__cell_21__a.T' : 0,
	'op_addsub__op_addsub__cell_21__a.F' : 0,
	'op_addsub__op_addsub__cell_20__onehot00' : 0,
	'op_addsub__op_addsub__cell_20__onehot01' : 0,
	'op_addsub__op_addsub__cell_20__onehot10' : 0,
	'op_addsub__op_addsub__cell_20__onehot11' : 0,
	'op_addsub__op_addsub__cell_21__b.T' : 0,
	'op_addsub__op_addsub__cell_21__b.F' : 0,
	'op_addsub__op_addsub__cell_21__onehot00' : 0,
	'op_addsub__op_addsub__cell_21__onehot01' : 0,
	'op_addsub__op_addsub__cell_21__onehot10' : 0,
	'op_addsub__op_addsub__cell_21__onehot11' : 0,
	'op_addsub__op_addsub__cell_22__b.T' : 0,
	'op_addsub__op_addsub__cell_22__b.F' : 0,
	'op_addsub__op_addsub__cell_22__onehot00' : 0,
	'op_addsub__op_addsub__cell_22__onehot01' : 0,
	'op_addsub__op_addsub__cell_22__onehot10' : 0,
	'op_addsub__op_addsub__cell_22__onehot11' : 0,
	'b1__c_b_out_2' : 1,
	'm__chA_z(1).T' : 0,
	'b2__z_in(1).T' : 0,
	'm__chA_z(0).T' : 0,
	'b1__c_a_out_3' : 1,
	'm__chA_z(2).F' : 0,
	'd2__chB_ack' : 0,
	'b1__c_a_out_0' : 1,
	'm__chA_z(1).F' : 0,
	'm__chA_z(3).T' : 0,
	'b1__c_b_out_3' : 1,
	'b2__z_in(2).F' : 0,
	'b1__c_b_out_0' : 1,
	'm__chB_z(0).T' : 0,
	'm__chA_z(0).F' : 0,
	'b2__z_in(0).F' : 0,
	'b1__c_a_out_1' : 1,
	'm__chB_z(2).T' : 0,
	'm__chB_z(3).T' : 0,
	'b2__z_in(1).F' : 0,
	'm__chB_z(1).T' : 0,
	'm__chA_z(2).T' : 0,
	'b2__z_in(3).F' : 0,
	'd2__trans1__chin_ack' : 0,
	'm__chA_z(3).F' : 0,
	'b1__c_op_out_0' : 1,
	'b1__c_b_out_1' : 1,
	'm__chB_done' : 0,
	'b1__c_a_out_2' : 1,
	'b1__c_op_out_1' : 1,
	'b2__z_in(2).T' : 0,
	'b2__z_in(0).T' : 0,
	'b1__ocd_n_lvl0_1' : 1,
	'd2__chA_ack' : 0,
	'b1__ocd_n_lvl0_4' : 1,
	'b2__z_in(3).T' : 0,
	'b1__ocd_n_lvl0_0' : 1,
	'd1__chB_ack' : 0,
	'b1__ocd_n_lvl0_3' : 1,
	'b1__ocd_n_lvl0_2' : 1,
	'm__chA_done' : 0,
	'd1__chA_ack' : 0,
	'b1__ocd_n_lvl1_0' : 1,
	'b1__en' : 1,
	'b1__ocd_n_lvl1_1' : 1,
	'b1__ocd_n_lvl2_0' : 1,
	'b1__ocd_n' : 1,
	'ack_out' : 0,
	}

	events = []

	tokens = [{'op': 2, 'a': 1, 'b': 3},
		   {'op': 2, 'a': 3, 'b': 11},
		   {'op': 0, 'a': 7, 'b': 12},
		   {'op': 1, 'a': 8, 'b': 2},
		   {'op': 1, 'a': 15, 'b': 1},
		   {'op': 0, 'a': 9, 'b': 4},
		   {'op': 2, 'a': 9, 'b': 10},
		   {'op': 3, 'a': 10, 'b': 5}]
	# , {'op': 2, 'a': 3, 'b': 11}, {'op': 0, 'a': 7, 'b': 12}, {'op': 1, 'a': 8, 'b': 2}, {'op': 1, 'a': 15, 'b': 1}, {'op': 0, 'a': 9, 'b': 4}, {'op': 2, 'a': 9, 'b': 10}, {'op': 3, 'a': 10, 'b': 5}

	input_widths = {'op': 2, 'a': 4, 'b': 4}

	output_signals = {'z(3).F', 'z(2).F', 'z(1).F', 'ack_out', 'z(1).T', 'z(3).T', 'z(0).T', 'z(0).F', 'z(2).T'}

	output_widths = {'z': 4}

	return init, events, tokens, input_widths, output_signals, output_widths
