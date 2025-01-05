from seal import tracem as tr

def GeneratePipeline():

	tr.rise(f=tr.NORr, i=['d1__chin_op.T', 'd1__chin_op.F'], o='b1__c_op_out_0', d=0.6773339463914112)
	tr.fall(f=tr.NORf, i=['d1__chin_op.T', 'd1__chin_op.F'], o='b1__c_op_out_0', d=0.6773339463914112)

	tr.rise(f=tr.Cr, i=['op(0).F', 'b1__en'], o='d1__chin_op.F', d=1.2824882613901563)
	tr.fall(f=tr.Cf, i=['op(0).F', 'b1__en'], o='d1__chin_op.F', d=1.2824882613901563)

	tr.rise(f=tr.Cr, i=['op(0).T', 'b1__en'], o='d1__chin_op.T', d=0.7138367491104487)
	tr.fall(f=tr.Cf, i=['op(0).T', 'b1__en'], o='d1__chin_op.T', d=0.7138367491104487)

	tr.rise(f=tr.NORr, i=['d1__cntrl_select.T', 'd1__cntrl_select.F'], o='b1__c_op_out_1', d=1.3430717900771794)
	tr.fall(f=tr.NORf, i=['d1__cntrl_select.T', 'd1__cntrl_select.F'], o='b1__c_op_out_1', d=1.3430717900771794)

	tr.rise(f=tr.Cr, i=['b1__en', 'op(1).F'], o='d1__cntrl_select.F', d=1.2239564152086637)
	tr.fall(f=tr.Cf, i=['b1__en', 'op(1).F'], o='d1__cntrl_select.F', d=1.2239564152086637)

	tr.rise(f=tr.Cr, i=['op(1).T', 'b1__en'], o='d1__cntrl_select.T', d=1.3320710338857193)
	tr.fall(f=tr.Cf, i=['op(1).T', 'b1__en'], o='d1__cntrl_select.T', d=1.3320710338857193)

	tr.rise(f=tr.NORr, i=['d1__chin_a(0).T', 'd1__chin_a(0).F'], o='b1__c_a_out_0', d=1.3456276596715124)
	tr.fall(f=tr.NORf, i=['d1__chin_a(0).T', 'd1__chin_a(0).F'], o='b1__c_a_out_0', d=1.3456276596715124)

	tr.rise(f=tr.Cr, i=['b1__en', 'a(0).F'], o='d1__chin_a(0).F', d=1.3273052608984033)
	tr.fall(f=tr.Cf, i=['b1__en', 'a(0).F'], o='d1__chin_a(0).F', d=1.3273052608984033)

	tr.rise(f=tr.Cr, i=['a(0).T', 'b1__en'], o='d1__chin_a(0).T', d=0.5769525104759125)
	tr.fall(f=tr.Cf, i=['a(0).T', 'b1__en'], o='d1__chin_a(0).T', d=0.5769525104759125)

	tr.rise(f=tr.NORr, i=['d1__chin_a(1).T', 'd1__chin_a(1).F'], o='b1__c_a_out_1', d=0.8769624871035097)
	tr.fall(f=tr.NORf, i=['d1__chin_a(1).T', 'd1__chin_a(1).F'], o='b1__c_a_out_1', d=0.8769624871035097)

	tr.rise(f=tr.Cr, i=['b1__en', 'a(1).F'], o='d1__chin_a(1).F', d=0.8485915921382002)
	tr.fall(f=tr.Cf, i=['b1__en', 'a(1).F'], o='d1__chin_a(1).F', d=0.8485915921382002)

	tr.rise(f=tr.Cr, i=['a(1).T', 'b1__en'], o='d1__chin_a(1).T', d=0.6281969865121662)
	tr.fall(f=tr.Cf, i=['a(1).T', 'b1__en'], o='d1__chin_a(1).T', d=0.6281969865121662)

	tr.rise(f=tr.NORr, i=['d1__chin_a(2).F', 'd1__chin_a(2).T'], o='b1__c_a_out_2', d=0.7143854800869623)
	tr.fall(f=tr.NORf, i=['d1__chin_a(2).F', 'd1__chin_a(2).T'], o='b1__c_a_out_2', d=0.7143854800869623)

	tr.rise(f=tr.Cr, i=['b1__en', 'a(2).F'], o='d1__chin_a(2).F', d=1.3071755016811912)
	tr.fall(f=tr.Cf, i=['b1__en', 'a(2).F'], o='d1__chin_a(2).F', d=1.3071755016811912)

	tr.rise(f=tr.Cr, i=['b1__en', 'a(2).T'], o='d1__chin_a(2).T', d=0.5087039164770043)
	tr.fall(f=tr.Cf, i=['b1__en', 'a(2).T'], o='d1__chin_a(2).T', d=0.5087039164770043)

	tr.rise(f=tr.NORr, i=['d1__chin_a(3).F', 'd1__chin_a(3).T'], o='b1__c_a_out_3', d=1.0034233640611538)
	tr.fall(f=tr.NORf, i=['d1__chin_a(3).F', 'd1__chin_a(3).T'], o='b1__c_a_out_3', d=1.0034233640611538)

	tr.rise(f=tr.Cr, i=['a(3).F', 'b1__en'], o='d1__chin_a(3).F', d=0.7555563690493102)
	tr.fall(f=tr.Cf, i=['a(3).F', 'b1__en'], o='d1__chin_a(3).F', d=0.7555563690493102)

	tr.rise(f=tr.Cr, i=['a(3).T', 'b1__en'], o='d1__chin_a(3).T', d=1.4253106097964134)
	tr.fall(f=tr.Cf, i=['a(3).T', 'b1__en'], o='d1__chin_a(3).T', d=1.4253106097964134)

	tr.rise(f=tr.NORr, i=['d1__chin_b(0).T', 'd1__chin_b(0).F'], o='b1__c_b_out_0', d=1.3060226471652623)
	tr.fall(f=tr.NORf, i=['d1__chin_b(0).T', 'd1__chin_b(0).F'], o='b1__c_b_out_0', d=1.3060226471652623)

	tr.rise(f=tr.Cr, i=['b(0).F', 'b1__en'], o='d1__chin_b(0).F', d=0.8027563931007476)
	tr.fall(f=tr.Cf, i=['b(0).F', 'b1__en'], o='d1__chin_b(0).F', d=0.8027563931007476)

	tr.rise(f=tr.Cr, i=['b(0).T', 'b1__en'], o='d1__chin_b(0).T', d=0.6797151916273378)
	tr.fall(f=tr.Cf, i=['b(0).T', 'b1__en'], o='d1__chin_b(0).T', d=0.6797151916273378)

	tr.rise(f=tr.NORr, i=['d1__chin_b(1).T', 'd1__chin_b(1).F'], o='b1__c_b_out_1', d=1.082377768235356)
	tr.fall(f=tr.NORf, i=['d1__chin_b(1).T', 'd1__chin_b(1).F'], o='b1__c_b_out_1', d=1.082377768235356)

	tr.rise(f=tr.Cr, i=['b(1).F', 'b1__en'], o='d1__chin_b(1).F', d=1.1446206057398054)
	tr.fall(f=tr.Cf, i=['b(1).F', 'b1__en'], o='d1__chin_b(1).F', d=1.1446206057398054)

	tr.rise(f=tr.Cr, i=['b1__en', 'b(1).T'], o='d1__chin_b(1).T', d=0.5749508727771283)
	tr.fall(f=tr.Cf, i=['b1__en', 'b(1).T'], o='d1__chin_b(1).T', d=0.5749508727771283)

	tr.rise(f=tr.NORr, i=['d1__chin_b(2).F', 'd1__chin_b(2).T'], o='b1__c_b_out_2', d=0.7201932310128659)
	tr.fall(f=tr.NORf, i=['d1__chin_b(2).F', 'd1__chin_b(2).T'], o='b1__c_b_out_2', d=0.7201932310128659)

	tr.rise(f=tr.Cr, i=['b(2).F', 'b1__en'], o='d1__chin_b(2).F', d=0.7523420920091438)
	tr.fall(f=tr.Cf, i=['b(2).F', 'b1__en'], o='d1__chin_b(2).F', d=0.7523420920091438)

	tr.rise(f=tr.Cr, i=['b(2).T', 'b1__en'], o='d1__chin_b(2).T', d=1.364754488495749)
	tr.fall(f=tr.Cf, i=['b(2).T', 'b1__en'], o='d1__chin_b(2).T', d=1.364754488495749)

	tr.rise(f=tr.NORr, i=['d1__chin_b(3).F', 'd1__chin_b(3).T'], o='b1__c_b_out_3', d=0.9283860965710902)
	tr.fall(f=tr.NORf, i=['d1__chin_b(3).F', 'd1__chin_b(3).T'], o='b1__c_b_out_3', d=0.9283860965710902)

	tr.rise(f=tr.Cr, i=['b(3).F', 'b1__en'], o='d1__chin_b(3).F', d=0.9695875784330792)
	tr.fall(f=tr.Cf, i=['b(3).F', 'b1__en'], o='d1__chin_b(3).F', d=0.9695875784330792)

	tr.rise(f=tr.Cr, i=['b(3).T', 'b1__en'], o='d1__chin_b(3).T', d=0.8309477848126359)
	tr.fall(f=tr.Cf, i=['b(3).T', 'b1__en'], o='d1__chin_b(3).T', d=0.8309477848126359)

	tr.rise(f=tr.Cr, i=['b1__c_op_out_0', 'b1__c_op_out_1'], o='b1__ocd_n_lvl0_0', d=1.177767203148126)
	tr.fall(f=tr.Cf, i=['b1__c_op_out_0', 'b1__c_op_out_1'], o='b1__ocd_n_lvl0_0', d=1.177767203148126)

	tr.rise(f=tr.Cr, i=['b1__c_a_out_0', 'b1__c_a_out_1'], o='b1__ocd_n_lvl0_1', d=1.431285362315572)
	tr.fall(f=tr.Cf, i=['b1__c_a_out_0', 'b1__c_a_out_1'], o='b1__ocd_n_lvl0_1', d=1.431285362315572)

	tr.rise(f=tr.Cr, i=['b1__c_a_out_2', 'b1__c_a_out_3'], o='b1__ocd_n_lvl0_2', d=0.8256867166201395)
	tr.fall(f=tr.Cf, i=['b1__c_a_out_2', 'b1__c_a_out_3'], o='b1__ocd_n_lvl0_2', d=0.8256867166201395)

	tr.rise(f=tr.Cr, i=['b1__c_b_out_1', 'b1__c_b_out_0'], o='b1__ocd_n_lvl0_3', d=0.8186842754192425)
	tr.fall(f=tr.Cf, i=['b1__c_b_out_1', 'b1__c_b_out_0'], o='b1__ocd_n_lvl0_3', d=0.8186842754192425)

	tr.rise(f=tr.Cr, i=['b1__c_b_out_2', 'b1__c_b_out_3'], o='b1__ocd_n_lvl0_4', d=1.0296686329521267)
	tr.fall(f=tr.Cf, i=['b1__c_b_out_2', 'b1__c_b_out_3'], o='b1__ocd_n_lvl0_4', d=1.0296686329521267)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_0', 'b1__ocd_n_lvl0_1'], o='b1__ocd_n_lvl1_0', d=1.415704009032847)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_0', 'b1__ocd_n_lvl0_1'], o='b1__ocd_n_lvl1_0', d=1.415704009032847)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_2', 'b1__ocd_n_lvl0_3'], o='b1__ocd_n_lvl1_1', d=0.8155812735220204)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_2', 'b1__ocd_n_lvl0_3'], o='b1__ocd_n_lvl1_1', d=0.8155812735220204)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl1_1', 'b1__ocd_n_lvl1_0'], o='b1__ocd_n_lvl2_0', d=1.0100502394656847)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl1_1', 'b1__ocd_n_lvl1_0'], o='b1__ocd_n_lvl2_0', d=1.0100502394656847)

	tr.rise(f=tr.Cr, i=['b1__ocd_n_lvl0_4', 'b1__ocd_n_lvl2_0'], o='b1__ocd_n', d=1.052756606981156)
	tr.fall(f=tr.Cf, i=['b1__ocd_n_lvl0_4', 'b1__ocd_n_lvl2_0'], o='b1__ocd_n', d=1.052756606981156)

	tr.rise(f=tr.INVr, i=['b1__ocd_n'], o='ack_out', d=0.8575456125204103)
	tr.fall(f=tr.INVf, i=['b1__ocd_n'], o='ack_out', d=0.8575456125204103)

	tr.rise(f=tr.NORr, i=['z(0).T', 'z(0).F'], o='b2__c_z_out_0', d=0.8403186931755843)
	tr.fall(f=tr.NORf, i=['z(0).T', 'z(0).F'], o='b2__c_z_out_0', d=0.8403186931755843)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__z_in(0).F'], o='z(0).F', d=1.2264208615749497)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__z_in(0).F'], o='z(0).F', d=1.2264208615749497)

	tr.rise(f=tr.Cr, i=['b2__z_in(0).T', 'b2__en'], o='z(0).T', d=0.5441440987298175)
	tr.fall(f=tr.Cf, i=['b2__z_in(0).T', 'b2__en'], o='z(0).T', d=0.5441440987298175)

	tr.rise(f=tr.NORr, i=['z(1).F', 'z(1).T'], o='b2__c_z_out_1', d=0.647322072104252)
	tr.fall(f=tr.NORf, i=['z(1).F', 'z(1).T'], o='b2__c_z_out_1', d=0.647322072104252)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__z_in(1).F'], o='z(1).F', d=0.6026723459928989)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__z_in(1).F'], o='z(1).F', d=0.6026723459928989)

	tr.rise(f=tr.Cr, i=['b2__z_in(1).T', 'b2__en'], o='z(1).T', d=0.6355985905432093)
	tr.fall(f=tr.Cf, i=['b2__z_in(1).T', 'b2__en'], o='z(1).T', d=0.6355985905432093)

	tr.rise(f=tr.NORr, i=['z(2).F', 'z(2).T'], o='b2__c_z_out_2', d=0.5183126182902644)
	tr.fall(f=tr.NORf, i=['z(2).F', 'z(2).T'], o='b2__c_z_out_2', d=0.5183126182902644)

	tr.rise(f=tr.Cr, i=['b2__en', 'b2__z_in(2).F'], o='z(2).F', d=1.3891613631528428)
	tr.fall(f=tr.Cf, i=['b2__en', 'b2__z_in(2).F'], o='z(2).F', d=1.3891613631528428)

	tr.rise(f=tr.Cr, i=['b2__z_in(2).T', 'b2__en'], o='z(2).T', d=1.4164232342576866)
	tr.fall(f=tr.Cf, i=['b2__z_in(2).T', 'b2__en'], o='z(2).T', d=1.4164232342576866)

	tr.rise(f=tr.NORr, i=['z(3).F', 'z(3).T'], o='b2__c_z_out_3', d=1.3260008421211347)
	tr.fall(f=tr.NORf, i=['z(3).F', 'z(3).T'], o='b2__c_z_out_3', d=1.3260008421211347)

	tr.rise(f=tr.Cr, i=['b2__z_in(3).F', 'b2__en'], o='z(3).F', d=0.619253903172456)
	tr.fall(f=tr.Cf, i=['b2__z_in(3).F', 'b2__en'], o='z(3).F', d=0.619253903172456)

	tr.rise(f=tr.Cr, i=['b2__z_in(3).T', 'b2__en'], o='z(3).T', d=1.2118445423177886)
	tr.fall(f=tr.Cf, i=['b2__z_in(3).T', 'b2__en'], o='z(3).T', d=1.2118445423177886)

	tr.rise(f=tr.Cr, i=['b2__c_z_out_0', 'b2__c_z_out_1'], o='b2__ocd_n_lvl0_0', d=1.0378337119885332)
	tr.fall(f=tr.Cf, i=['b2__c_z_out_0', 'b2__c_z_out_1'], o='b2__ocd_n_lvl0_0', d=1.0378337119885332)

	tr.rise(f=tr.Cr, i=['b2__c_z_out_2', 'b2__c_z_out_3'], o='b2__ocd_n_lvl0_1', d=0.5534683088758671)
	tr.fall(f=tr.Cf, i=['b2__c_z_out_2', 'b2__c_z_out_3'], o='b2__ocd_n_lvl0_1', d=0.5534683088758671)

	tr.rise(f=tr.Cr, i=['b2__ocd_n_lvl0_1', 'b2__ocd_n_lvl0_0'], o='b2__ocd_n', d=1.1131007017760561)
	tr.fall(f=tr.Cf, i=['b2__ocd_n_lvl0_1', 'b2__ocd_n_lvl0_0'], o='b2__ocd_n', d=1.1131007017760561)

	tr.rise(f=tr.INVr, i=['b2__ocd_n'], o='m__chout_ack', d=0.6589160675157963)
	tr.fall(f=tr.INVf, i=['b2__ocd_n'], o='m__chout_ack', d=0.6589160675157963)

	tr.rise(f=tr.INVr, i=['ack_in'], o='b2__en', d=1.1072428354127353)
	tr.fall(f=tr.INVf, i=['ack_in'], o='b2__en', d=1.1072428354127353)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_a(3).T'], o='op_addsub__op_addsub__a(3).T', d=0.9724083878326039)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_a(3).T'], o='op_addsub__op_addsub__a(3).T', d=0.9724083878326039)

	tr.rise(f=tr.Cr, i=['d1__chin_a(3).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(3).F', d=0.5216409481526164)
	tr.fall(f=tr.Cf, i=['d1__chin_a(3).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(3).F', d=0.5216409481526164)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(0).T'], o='op_addsub__op_addsub__b(0).T', d=0.5700449566565772)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(0).T'], o='op_addsub__op_addsub__b(0).T', d=0.5700449566565772)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(0).F'], o='op_addsub__op_addsub__b(0).F', d=0.8907904805088275)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(0).F'], o='op_addsub__op_addsub__b(0).F', d=0.8907904805088275)

	tr.rise(f=tr.Cr, i=['d1__chin_a(1).T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(1).T', d=0.9112469884036434)
	tr.fall(f=tr.Cf, i=['d1__chin_a(1).T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(1).T', d=0.9112469884036434)

	tr.rise(f=tr.Cr, i=['d1__chin_a(1).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(1).F', d=0.5417775462418806)
	tr.fall(f=tr.Cf, i=['d1__chin_a(1).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(1).F', d=0.5417775462418806)

	tr.rise(f=tr.Cr, i=['d1__chin_op.T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__op.T', d=0.8028159736918474)
	tr.fall(f=tr.Cf, i=['d1__chin_op.T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__op.T', d=0.8028159736918474)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_op.F'], o='op_addsub__op_addsub__op.F', d=1.274008885065101)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_op.F'], o='op_addsub__op_addsub__op.F', d=1.274008885065101)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_a(2).T'], o='op_addsub__op_addsub__a(2).T', d=1.4312747479773398)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_a(2).T'], o='op_addsub__op_addsub__a(2).T', d=1.4312747479773398)

	tr.rise(f=tr.Cr, i=['d1__chin_a(2).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(2).F', d=0.511314034124194)
	tr.fall(f=tr.Cf, i=['d1__chin_a(2).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(2).F', d=0.511314034124194)

	tr.rise(f=tr.Cr, i=['d1__chin_a(0).T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(0).T', d=1.4192853565784178)
	tr.fall(f=tr.Cf, i=['d1__chin_a(0).T', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__a(0).T', d=1.4192853565784178)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_a(0).F'], o='op_addsub__op_addsub__a(0).F', d=0.6020526356800728)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_a(0).F'], o='op_addsub__op_addsub__a(0).F', d=0.6020526356800728)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(3).T'], o='op_addsub__op_addsub__b(3).T', d=1.382679907618938)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(3).T'], o='op_addsub__op_addsub__b(3).T', d=1.382679907618938)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(3).F'], o='op_addsub__op_addsub__b(3).F', d=1.3729146672649066)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(3).F'], o='op_addsub__op_addsub__b(3).F', d=1.3729146672649066)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(1).T'], o='op_addsub__op_addsub__b(1).T', d=0.7290839279559412)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(1).T'], o='op_addsub__op_addsub__b(1).T', d=0.7290839279559412)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(1).F'], o='op_addsub__op_addsub__b(1).F', d=0.5683172872516791)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(1).F'], o='op_addsub__op_addsub__b(1).F', d=0.5683172872516791)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.F', 'd1__chin_b(2).T'], o='op_addsub__op_addsub__b(2).T', d=0.9696952598270028)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.F', 'd1__chin_b(2).T'], o='op_addsub__op_addsub__b(2).T', d=0.9696952598270028)

	tr.rise(f=tr.Cr, i=['d1__chin_b(2).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__b(2).F', d=0.9881954889284428)
	tr.fall(f=tr.Cf, i=['d1__chin_b(2).F', 'd1__cntrl_select.F'], o='op_addsub__op_addsub__b(2).F', d=0.9881954889284428)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(3).T'], o='d2__chin_a(3).T', d=1.23585011731583)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(3).T'], o='d2__chin_a(3).T', d=1.23585011731583)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(3).F'], o='d2__chin_a(3).F', d=0.8155389291543579)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(3).F'], o='d2__chin_a(3).F', d=0.8155389291543579)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(0).T'], o='d2__chin_b(0).T', d=0.9552445756358203)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(0).T'], o='d2__chin_b(0).T', d=0.9552445756358203)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(0).F'], o='d2__chin_b(0).F', d=1.1404771334813475)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(0).F'], o='d2__chin_b(0).F', d=1.1404771334813475)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(1).T'], o='d2__chin_a(1).T', d=1.3410235559239558)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(1).T'], o='d2__chin_a(1).T', d=1.3410235559239558)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(1).F'], o='d2__chin_a(1).F', d=1.2490213166728175)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(1).F'], o='d2__chin_a(1).F', d=1.2490213166728175)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_op.T'], o='d2__cntrl_select.T', d=1.2553588936457052)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_op.T'], o='d2__cntrl_select.T', d=1.2553588936457052)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_op.F'], o='d2__cntrl_select.F', d=1.4513787368667925)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_op.F'], o='d2__cntrl_select.F', d=1.4513787368667925)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(2).T'], o='d2__chin_a(2).T', d=0.8972038643732109)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(2).T'], o='d2__chin_a(2).T', d=0.8972038643732109)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(2).F'], o='d2__chin_a(2).F', d=1.0575480792393996)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(2).F'], o='d2__chin_a(2).F', d=1.0575480792393996)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(0).T'], o='d2__chin_a(0).T', d=0.7665462663231416)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(0).T'], o='d2__chin_a(0).T', d=0.7665462663231416)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_a(0).F'], o='d2__chin_a(0).F', d=1.118752642561987)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_a(0).F'], o='d2__chin_a(0).F', d=1.118752642561987)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(3).T'], o='d2__chin_b(3).T', d=0.5796721480664463)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(3).T'], o='d2__chin_b(3).T', d=0.5796721480664463)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(3).F'], o='d2__chin_b(3).F', d=1.0149392030210027)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(3).F'], o='d2__chin_b(3).F', d=1.0149392030210027)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(1).T'], o='d2__chin_b(1).T', d=1.0003568658171322)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(1).T'], o='d2__chin_b(1).T', d=1.0003568658171322)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(1).F'], o='d2__chin_b(1).F', d=0.7181247703062522)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(1).F'], o='d2__chin_b(1).F', d=0.7181247703062522)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(2).T'], o='d2__chin_b(2).T', d=1.2791815149575183)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(2).T'], o='d2__chin_b(2).T', d=1.2791815149575183)

	tr.rise(f=tr.Cr, i=['d1__cntrl_select.T', 'd1__chin_b(2).F'], o='d2__chin_b(2).F', d=1.3734894446675168)
	tr.fall(f=tr.Cf, i=['d1__cntrl_select.T', 'd1__chin_b(2).F'], o='d2__chin_b(2).F', d=1.3734894446675168)

	tr.rise(f=tr.NORr, i=['d1__chB_ack', 'd1__chA_ack'], o='b1__en', d=0.9361264462883571)
	tr.fall(f=tr.NORf, i=['d1__chB_ack', 'd1__chA_ack'], o='b1__en', d=0.9361264462883571)

	tr.rise(f=tr.Cr, i=['d2__chin_a(3).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(3).T', d=1.4132915601957619)
	tr.fall(f=tr.Cf, i=['d2__chin_a(3).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(3).T', d=1.4132915601957619)

	tr.rise(f=tr.Cr, i=['d2__chin_a(3).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(3).F', d=1.4155898490098662)
	tr.fall(f=tr.Cf, i=['d2__chin_a(3).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(3).F', d=1.4155898490098662)

	tr.rise(f=tr.Cr, i=['d2__chin_b(0).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(0).T', d=0.9857264568086801)
	tr.fall(f=tr.Cf, i=['d2__chin_b(0).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(0).T', d=0.9857264568086801)

	tr.rise(f=tr.Cr, i=['d2__chin_b(0).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(0).F', d=1.233893817962291)
	tr.fall(f=tr.Cf, i=['d2__chin_b(0).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(0).F', d=1.233893817962291)

	tr.rise(f=tr.Cr, i=['d2__chin_a(1).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(1).T', d=0.5746470450533763)
	tr.fall(f=tr.Cf, i=['d2__chin_a(1).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(1).T', d=0.5746470450533763)

	tr.rise(f=tr.Cr, i=['d2__chin_a(1).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(1).F', d=0.7237893727650339)
	tr.fall(f=tr.Cf, i=['d2__chin_a(1).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(1).F', d=0.7237893727650339)

	tr.rise(f=tr.Cr, i=['d2__chin_a(2).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(2).T', d=0.7853484051066696)
	tr.fall(f=tr.Cf, i=['d2__chin_a(2).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(2).T', d=0.7853484051066696)

	tr.rise(f=tr.Cr, i=['d2__chin_a(2).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(2).F', d=0.8841951735992813)
	tr.fall(f=tr.Cf, i=['d2__chin_a(2).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(2).F', d=0.8841951735992813)

	tr.rise(f=tr.Cr, i=['d2__chin_a(0).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(0).T', d=1.3480878517404071)
	tr.fall(f=tr.Cf, i=['d2__chin_a(0).T', 'd2__cntrl_select.F'], o='op_or__op_or__a(0).T', d=1.3480878517404071)

	tr.rise(f=tr.Cr, i=['d2__chin_a(0).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(0).F', d=1.4470147184296371)
	tr.fall(f=tr.Cf, i=['d2__chin_a(0).F', 'd2__cntrl_select.F'], o='op_or__op_or__a(0).F', d=1.4470147184296371)

	tr.rise(f=tr.Cr, i=['d2__chin_b(3).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(3).T', d=0.590129504748731)
	tr.fall(f=tr.Cf, i=['d2__chin_b(3).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(3).T', d=0.590129504748731)

	tr.rise(f=tr.Cr, i=['d2__chin_b(3).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(3).F', d=0.5866379489294856)
	tr.fall(f=tr.Cf, i=['d2__chin_b(3).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(3).F', d=0.5866379489294856)

	tr.rise(f=tr.Cr, i=['d2__chin_b(1).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(1).T', d=1.3708691072499297)
	tr.fall(f=tr.Cf, i=['d2__chin_b(1).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(1).T', d=1.3708691072499297)

	tr.rise(f=tr.Cr, i=['d2__chin_b(1).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(1).F', d=0.7215308435954155)
	tr.fall(f=tr.Cf, i=['d2__chin_b(1).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(1).F', d=0.7215308435954155)

	tr.rise(f=tr.Cr, i=['d2__chin_b(2).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(2).T', d=1.4766337031202934)
	tr.fall(f=tr.Cf, i=['d2__chin_b(2).T', 'd2__cntrl_select.F'], o='op_or__op_or__b(2).T', d=1.4766337031202934)

	tr.rise(f=tr.Cr, i=['d2__chin_b(2).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(2).F', d=0.9461938536212203)
	tr.fall(f=tr.Cf, i=['d2__chin_b(2).F', 'd2__cntrl_select.F'], o='op_or__op_or__b(2).F', d=0.9461938536212203)

	tr.rise(f=tr.Cr, i=['d2__cntrl_select.T', 'd2__chin_a(3).T'], o='m__chC_z(3).F', d=1.2357085714227707)
	tr.fall(f=tr.Cf, i=['d2__cntrl_select.T', 'd2__chin_a(3).T'], o='m__chC_z(3).F', d=1.2357085714227707)

	tr.rise(f=tr.Cr, i=['d2__chin_a(3).F', 'd2__cntrl_select.T'], o='m__chC_z(3).T', d=1.3823089634096593)
	tr.fall(f=tr.Cf, i=['d2__chin_a(3).F', 'd2__cntrl_select.T'], o='m__chC_z(3).T', d=1.3823089634096593)

	tr.rise(f=tr.Cr, i=['d2__chin_b(0).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(0).T', d=0.9908182987636102)
	tr.fall(f=tr.Cf, i=['d2__chin_b(0).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(0).T', d=0.9908182987636102)

	tr.rise(f=tr.Cr, i=['d2__chin_b(0).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(0).F', d=0.7472269739817041)
	tr.fall(f=tr.Cf, i=['d2__chin_b(0).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(0).F', d=0.7472269739817041)

	tr.rise(f=tr.Cr, i=['d2__chin_a(1).T', 'd2__cntrl_select.T'], o='m__chC_z(1).F', d=1.2982514711229864)
	tr.fall(f=tr.Cf, i=['d2__chin_a(1).T', 'd2__cntrl_select.T'], o='m__chC_z(1).F', d=1.2982514711229864)

	tr.rise(f=tr.Cr, i=['d2__chin_a(1).F', 'd2__cntrl_select.T'], o='m__chC_z(1).T', d=1.2210627242448977)
	tr.fall(f=tr.Cf, i=['d2__chin_a(1).F', 'd2__cntrl_select.T'], o='m__chC_z(1).T', d=1.2210627242448977)

	tr.rise(f=tr.Cr, i=['d2__cntrl_select.T', 'd2__chin_a(2).T'], o='m__chC_z(2).F', d=1.0754815815811676)
	tr.fall(f=tr.Cf, i=['d2__cntrl_select.T', 'd2__chin_a(2).T'], o='m__chC_z(2).F', d=1.0754815815811676)

	tr.rise(f=tr.Cr, i=['d2__chin_a(2).F', 'd2__cntrl_select.T'], o='m__chC_z(2).T', d=0.7246766594255103)
	tr.fall(f=tr.Cf, i=['d2__chin_a(2).F', 'd2__cntrl_select.T'], o='m__chC_z(2).T', d=0.7246766594255103)

	tr.rise(f=tr.Cr, i=['d2__chin_a(0).T', 'd2__cntrl_select.T'], o='m__chC_z(0).F', d=0.62966838039217)
	tr.fall(f=tr.Cf, i=['d2__chin_a(0).T', 'd2__cntrl_select.T'], o='m__chC_z(0).F', d=0.62966838039217)

	tr.rise(f=tr.Cr, i=['d2__chin_a(0).F', 'd2__cntrl_select.T'], o='m__chC_z(0).T', d=1.128187367048421)
	tr.fall(f=tr.Cf, i=['d2__chin_a(0).F', 'd2__cntrl_select.T'], o='m__chC_z(0).T', d=1.128187367048421)

	tr.rise(f=tr.Cr, i=['d2__chin_b(3).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(3).T', d=1.1795785444615576)
	tr.fall(f=tr.Cf, i=['d2__chin_b(3).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(3).T', d=1.1795785444615576)

	tr.rise(f=tr.Cr, i=['d2__chin_b(3).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(3).F', d=0.539382522750784)
	tr.fall(f=tr.Cf, i=['d2__chin_b(3).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(3).F', d=0.539382522750784)

	tr.rise(f=tr.Cr, i=['d2__chin_b(1).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(1).T', d=1.485784177721762)
	tr.fall(f=tr.Cf, i=['d2__chin_b(1).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(1).T', d=1.485784177721762)

	tr.rise(f=tr.Cr, i=['d2__chin_b(1).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(1).F', d=0.546610570640562)
	tr.fall(f=tr.Cf, i=['d2__chin_b(1).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(1).F', d=0.546610570640562)

	tr.rise(f=tr.Cr, i=['d2__chin_b(2).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(2).T', d=0.633981217893924)
	tr.fall(f=tr.Cf, i=['d2__chin_b(2).T', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(2).T', d=0.633981217893924)

	tr.rise(f=tr.Cr, i=['d2__chin_b(2).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(2).F', d=0.8620185066860557)
	tr.fall(f=tr.Cf, i=['d2__chin_b(2).F', 'd2__cntrl_select.T'], o='d2__trans1__chin_b(2).F', d=0.8620185066860557)

	tr.rise(f=tr.ORr, i=['d2__trans1__chin_ack', 'd2__chA_ack'], o='d1__chB_ack', d=0.8763468982388588)
	tr.fall(f=tr.ORf, i=['d2__trans1__chin_ack', 'd2__chA_ack'], o='d1__chB_ack', d=0.8763468982388588)

	tr.rise(f=tr.NORr, i=['d2__trans1__chin_b(0).F', 'd2__trans1__chin_b(0).T'], o='d2__trans1__unused_cd_chin_b_0', d=1.0502482511425386)
	tr.fall(f=tr.NORf, i=['d2__trans1__chin_b(0).F', 'd2__trans1__chin_b(0).T'], o='d2__trans1__unused_cd_chin_b_0', d=1.0502482511425386)

	tr.rise(f=tr.NORr, i=['d2__trans1__chin_b(3).F', 'd2__trans1__chin_b(3).T'], o='d2__trans1__unused_cd_chin_b_3', d=0.83942145849682)
	tr.fall(f=tr.NORf, i=['d2__trans1__chin_b(3).F', 'd2__trans1__chin_b(3).T'], o='d2__trans1__unused_cd_chin_b_3', d=0.83942145849682)

	tr.rise(f=tr.NORr, i=['d2__trans1__chin_b(1).F', 'd2__trans1__chin_b(1).T'], o='d2__trans1__unused_cd_chin_b_1', d=0.7363251916365963)
	tr.fall(f=tr.NORf, i=['d2__trans1__chin_b(1).F', 'd2__trans1__chin_b(1).T'], o='d2__trans1__unused_cd_chin_b_1', d=0.7363251916365963)

	tr.rise(f=tr.NORr, i=['d2__trans1__chin_b(2).F', 'd2__trans1__chin_b(2).T'], o='d2__trans1__unused_cd_chin_b_2', d=0.6383858011649607)
	tr.fall(f=tr.NORf, i=['d2__trans1__chin_b(2).F', 'd2__trans1__chin_b(2).T'], o='d2__trans1__unused_cd_chin_b_2', d=0.6383858011649607)

	tr.rise(f=tr.Cr, i=['d2__trans1__unused_cd_chin_b_3', 'd2__trans1__unused_cd_chin_b_0'], o='d2__trans1__icd_n_lvl0_0', d=0.778650937181058)
	tr.fall(f=tr.Cf, i=['d2__trans1__unused_cd_chin_b_3', 'd2__trans1__unused_cd_chin_b_0'], o='d2__trans1__icd_n_lvl0_0', d=0.778650937181058)

	tr.rise(f=tr.Cr, i=['d2__trans1__unused_cd_chin_b_2', 'd2__trans1__unused_cd_chin_b_1'], o='d2__trans1__icd_n_lvl0_1', d=1.2779098874614845)
	tr.fall(f=tr.Cf, i=['d2__trans1__unused_cd_chin_b_2', 'd2__trans1__unused_cd_chin_b_1'], o='d2__trans1__icd_n_lvl0_1', d=1.2779098874614845)

	tr.rise(f=tr.Cr, i=['d2__trans1__icd_n_lvl0_1', 'd2__trans1__icd_n_lvl0_0'], o='d2__trans1__icd_n', d=1.3351259994721456)
	tr.fall(f=tr.Cf, i=['d2__trans1__icd_n_lvl0_1', 'd2__trans1__icd_n_lvl0_0'], o='d2__trans1__icd_n', d=1.3351259994721456)

	tr.rise(f=tr.INVr, i=['d2__trans1__icd_n'], o='d2__trans1__icd', d=0.6318642954748072)
	tr.fall(f=tr.INVf, i=['d2__trans1__icd_n'], o='d2__trans1__icd', d=0.6318642954748072)

	tr.rise(f=tr.Cr, i=['d2__chB_ack', 'd2__trans1__icd'], o='d2__trans1__chin_ack', d=0.9792057953238631)
	tr.fall(f=tr.Cf, i=['d2__chB_ack', 'd2__trans1__icd'], o='d2__trans1__chin_ack', d=0.9792057953238631)

	tr.rise(f=tr.ORr, i=['m__chA_z(3).F', 'm__chA_z(3).T'], o='m__chA_done', d=1.4345475787848043)
	tr.fall(f=tr.ORf, i=['m__chA_z(3).F', 'm__chA_z(3).T'], o='m__chA_done', d=1.4345475787848043)

	tr.rise(f=tr.Cr, i=['m__chout_ack', 'm__chA_done'], o='d1__chA_ack', d=1.1046832711887102)
	tr.fall(f=tr.Cf, i=['m__chout_ack', 'm__chA_done'], o='d1__chA_ack', d=1.1046832711887102)

	tr.rise(f=tr.ORr, i=['m__chB_z(2).F', 'm__chB_z(2).T'], o='m__chB_done', d=0.8611930371625042)
	tr.fall(f=tr.ORf, i=['m__chB_z(2).F', 'm__chB_z(2).T'], o='m__chB_done', d=0.8611930371625042)

	tr.rise(f=tr.Cr, i=['m__chB_done', 'm__chout_ack'], o='d2__chA_ack', d=0.5311078807361203)
	tr.fall(f=tr.Cf, i=['m__chB_done', 'm__chout_ack'], o='d2__chA_ack', d=0.5311078807361203)

	tr.rise(f=tr.ORr, i=['m__chC_z(2).F', 'm__chC_z(2).T'], o='m__chC_done', d=0.6671224042365268)
	tr.fall(f=tr.ORf, i=['m__chC_z(2).F', 'm__chC_z(2).T'], o='m__chC_done', d=0.6671224042365268)

	tr.rise(f=tr.Cr, i=['m__chC_done', 'm__chout_ack'], o='d2__chB_ack', d=1.3451631003778584)
	tr.fall(f=tr.Cf, i=['m__chC_done', 'm__chout_ack'], o='d2__chB_ack', d=1.3451631003778584)

	tr.rise(f=tr.ORr, i=['m__chB_z(3).T', 'm__chC_z(3).T', 'm__chA_z(3).T'], o='b2__z_in(3).T', d=0.7380273044675726)
	tr.fall(f=tr.ORf, i=['m__chB_z(3).T', 'm__chC_z(3).T', 'm__chA_z(3).T'], o='b2__z_in(3).T', d=0.7380273044675726)

	tr.rise(f=tr.ORr, i=['m__chB_z(3).F', 'm__chA_z(3).F', 'm__chC_z(3).F'], o='b2__z_in(3).F', d=1.3066576037904691)
	tr.fall(f=tr.ORf, i=['m__chB_z(3).F', 'm__chA_z(3).F', 'm__chC_z(3).F'], o='b2__z_in(3).F', d=1.3066576037904691)

	tr.rise(f=tr.ORr, i=['m__chA_z(1).T', 'm__chC_z(1).T', 'm__chB_z(1).T'], o='b2__z_in(1).T', d=0.7645327876535556)
	tr.fall(f=tr.ORf, i=['m__chA_z(1).T', 'm__chC_z(1).T', 'm__chB_z(1).T'], o='b2__z_in(1).T', d=0.7645327876535556)

	tr.rise(f=tr.ORr, i=['m__chA_z(1).F', 'm__chB_z(1).F', 'm__chC_z(1).F'], o='b2__z_in(1).F', d=0.7456850357038145)
	tr.fall(f=tr.ORf, i=['m__chA_z(1).F', 'm__chB_z(1).F', 'm__chC_z(1).F'], o='b2__z_in(1).F', d=0.7456850357038145)

	tr.rise(f=tr.ORr, i=['m__chB_z(0).T', 'm__chA_z(0).T', 'm__chC_z(0).T'], o='b2__z_in(0).T', d=1.0063460333403949)
	tr.fall(f=tr.ORf, i=['m__chB_z(0).T', 'm__chA_z(0).T', 'm__chC_z(0).T'], o='b2__z_in(0).T', d=1.0063460333403949)

	tr.rise(f=tr.ORr, i=['m__chC_z(0).F', 'm__chA_z(0).F', 'm__chB_z(0).F'], o='b2__z_in(0).F', d=0.77328568662303)
	tr.fall(f=tr.ORf, i=['m__chC_z(0).F', 'm__chA_z(0).F', 'm__chB_z(0).F'], o='b2__z_in(0).F', d=0.77328568662303)

	tr.rise(f=tr.ORr, i=['m__chA_z(2).T', 'm__chB_z(2).T', 'm__chC_z(2).T'], o='b2__z_in(2).T', d=1.10176793404618)
	tr.fall(f=tr.ORf, i=['m__chA_z(2).T', 'm__chB_z(2).T', 'm__chC_z(2).T'], o='b2__z_in(2).T', d=1.10176793404618)

	tr.rise(f=tr.ORr, i=['m__chB_z(2).F', 'm__chC_z(2).F', 'm__chA_z(2).F'], o='b2__z_in(2).F', d=1.4640303018539758)
	tr.fall(f=tr.ORf, i=['m__chB_z(2).F', 'm__chC_z(2).F', 'm__chA_z(2).F'], o='b2__z_in(2).F', d=1.4640303018539758)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(1).T', 'op_or__op_or__a(1).T'], o='op_or__op_or__cell_00__onehot00', d=1.207693810382867)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(1).T', 'op_or__op_or__a(1).T'], o='op_or__op_or__cell_00__onehot00', d=1.207693810382867)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(1).T', 'op_or__op_or__a(1).F'], o='op_or__op_or__cell_00__onehot01', d=0.6753957156310437)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(1).T', 'op_or__op_or__a(1).F'], o='op_or__op_or__cell_00__onehot01', d=0.6753957156310437)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(1).F', 'op_or__op_or__a(1).T'], o='op_or__op_or__cell_00__onehot10', d=0.7738748771055277)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(1).F', 'op_or__op_or__a(1).T'], o='op_or__op_or__cell_00__onehot10', d=0.7738748771055277)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(1).F', 'op_or__op_or__b(1).F'], o='m__chB_z(1).F', d=0.5479771501357471)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(1).F', 'op_or__op_or__b(1).F'], o='m__chB_z(1).F', d=0.5479771501357471)

	tr.rise(f=tr.ORr, i=['op_or__op_or__cell_00__onehot01', 'op_or__op_or__cell_00__onehot10', 'op_or__op_or__cell_00__onehot00'], o='m__chB_z(1).T', d=0.9202151645804151)
	tr.fall(f=tr.ORf, i=['op_or__op_or__cell_00__onehot01', 'op_or__op_or__cell_00__onehot10', 'op_or__op_or__cell_00__onehot00'], o='m__chB_z(1).T', d=0.9202151645804151)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(2).T', 'op_or__op_or__b(2).T'], o='op_or__op_or__cell_01__onehot00', d=1.2976094637807423)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(2).T', 'op_or__op_or__b(2).T'], o='op_or__op_or__cell_01__onehot00', d=1.2976094637807423)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(2).F', 'op_or__op_or__b(2).T'], o='op_or__op_or__cell_01__onehot01', d=0.8617375477948852)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(2).F', 'op_or__op_or__b(2).T'], o='op_or__op_or__cell_01__onehot01', d=0.8617375477948852)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(2).T', 'op_or__op_or__b(2).F'], o='op_or__op_or__cell_01__onehot10', d=1.3480262077686973)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(2).T', 'op_or__op_or__b(2).F'], o='op_or__op_or__cell_01__onehot10', d=1.3480262077686973)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(2).F', 'op_or__op_or__b(2).F'], o='m__chB_z(2).F', d=1.4115149459644023)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(2).F', 'op_or__op_or__b(2).F'], o='m__chB_z(2).F', d=1.4115149459644023)

	tr.rise(f=tr.ORr, i=['op_or__op_or__cell_01__onehot01', 'op_or__op_or__cell_01__onehot10', 'op_or__op_or__cell_01__onehot00'], o='m__chB_z(2).T', d=1.176498056324803)
	tr.fall(f=tr.ORf, i=['op_or__op_or__cell_01__onehot01', 'op_or__op_or__cell_01__onehot10', 'op_or__op_or__cell_01__onehot00'], o='m__chB_z(2).T', d=1.176498056324803)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(3).T', 'op_or__op_or__a(3).T'], o='op_or__op_or__cell_02__onehot00', d=1.2099133137463718)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(3).T', 'op_or__op_or__a(3).T'], o='op_or__op_or__cell_02__onehot00', d=1.2099133137463718)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(3).T', 'op_or__op_or__a(3).F'], o='op_or__op_or__cell_02__onehot01', d=0.7089522130141309)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(3).T', 'op_or__op_or__a(3).F'], o='op_or__op_or__cell_02__onehot01', d=0.7089522130141309)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(3).T', 'op_or__op_or__b(3).F'], o='op_or__op_or__cell_02__onehot10', d=0.7040586757750263)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(3).T', 'op_or__op_or__b(3).F'], o='op_or__op_or__cell_02__onehot10', d=0.7040586757750263)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(3).F', 'op_or__op_or__b(3).F'], o='m__chB_z(3).F', d=0.7992828034225686)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(3).F', 'op_or__op_or__b(3).F'], o='m__chB_z(3).F', d=0.7992828034225686)

	tr.rise(f=tr.ORr, i=['op_or__op_or__cell_02__onehot00', 'op_or__op_or__cell_02__onehot01', 'op_or__op_or__cell_02__onehot10'], o='m__chB_z(3).T', d=0.776372323592087)
	tr.fall(f=tr.ORf, i=['op_or__op_or__cell_02__onehot00', 'op_or__op_or__cell_02__onehot01', 'op_or__op_or__cell_02__onehot10'], o='m__chB_z(3).T', d=0.776372323592087)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(0).T', 'op_or__op_or__b(0).T'], o='op_or__op_or__cell_03__onehot00', d=0.7664351720819487)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(0).T', 'op_or__op_or__b(0).T'], o='op_or__op_or__cell_03__onehot00', d=0.7664351720819487)

	tr.rise(f=tr.Cr, i=['op_or__op_or__b(0).T', 'op_or__op_or__a(0).F'], o='op_or__op_or__cell_03__onehot01', d=0.5413262070837823)
	tr.fall(f=tr.Cf, i=['op_or__op_or__b(0).T', 'op_or__op_or__a(0).F'], o='op_or__op_or__cell_03__onehot01', d=0.5413262070837823)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(0).T', 'op_or__op_or__b(0).F'], o='op_or__op_or__cell_03__onehot10', d=0.7500200846133167)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(0).T', 'op_or__op_or__b(0).F'], o='op_or__op_or__cell_03__onehot10', d=0.7500200846133167)

	tr.rise(f=tr.Cr, i=['op_or__op_or__a(0).F', 'op_or__op_or__b(0).F'], o='m__chB_z(0).F', d=1.445419909256572)
	tr.fall(f=tr.Cf, i=['op_or__op_or__a(0).F', 'op_or__op_or__b(0).F'], o='m__chB_z(0).F', d=1.445419909256572)

	tr.rise(f=tr.ORr, i=['op_or__op_or__cell_03__onehot00', 'op_or__op_or__cell_03__onehot10', 'op_or__op_or__cell_03__onehot01'], o='m__chB_z(0).T', d=1.2421347399945353)
	tr.fall(f=tr.ORf, i=['op_or__op_or__cell_03__onehot00', 'op_or__op_or__cell_03__onehot10', 'op_or__op_or__cell_03__onehot01'], o='m__chB_z(0).T', d=1.2421347399945353)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__a(0).F'], o='op_addsub__op_addsub__cell_23__onehot00', d=1.3837817058394613)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__a(0).F'], o='op_addsub__op_addsub__cell_23__onehot00', d=1.3837817058394613)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__a(0).T'], o='op_addsub__op_addsub__cell_23__onehot01', d=0.5204661681908991)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__a(0).T'], o='op_addsub__op_addsub__cell_23__onehot01', d=0.5204661681908991)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__a(0).F'], o='op_addsub__op_addsub__cell_23__onehot10', d=1.291660287705691)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__a(0).F'], o='op_addsub__op_addsub__cell_23__onehot10', d=1.291660287705691)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__a(0).T'], o='op_addsub__op_addsub__cell_23__onehot11', d=0.7637413009849383)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__a(0).T'], o='op_addsub__op_addsub__cell_23__onehot11', d=0.7637413009849383)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_23__onehot10', 'op_addsub__op_addsub__cell_23__onehot01', 'op_addsub__op_addsub__cell_23__onehot00'], o='op_addsub__op_addsub__cell_10__a_F', d=1.0931910990083997)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_23__onehot10', 'op_addsub__op_addsub__cell_23__onehot01', 'op_addsub__op_addsub__cell_23__onehot00'], o='op_addsub__op_addsub__cell_10__a_F', d=1.0931910990083997)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_18__b.T', d=1.285788404249102)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_18__b.T', d=1.285788404249102)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_02__onehot10', d=1.4613371237607502)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_02__onehot10', d=1.4613371237607502)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_02__onehot01', d=1.1971612056152443)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).F', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_02__onehot01', d=1.1971612056152443)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_02__onehot00', d=0.7000733905855322)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(0).T', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_02__onehot00', d=0.7000733905855322)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_18__b.T', 'op_addsub__op_addsub__cell_02__onehot10', 'op_addsub__op_addsub__cell_02__onehot01'], o='op_addsub__op_addsub__cell_04__a_T', d=0.8146089911928424)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_18__b.T', 'op_addsub__op_addsub__cell_02__onehot10', 'op_addsub__op_addsub__cell_02__onehot01'], o='op_addsub__op_addsub__cell_04__a_T', d=0.8146089911928424)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_02__onehot00', 'op_addsub__op_addsub__cell_02__onehot10', 'op_addsub__op_addsub__cell_02__onehot01'], o='op_addsub__op_addsub__cell_18__b.F', d=0.5132154019559578)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_02__onehot00', 'op_addsub__op_addsub__cell_02__onehot10', 'op_addsub__op_addsub__cell_02__onehot01'], o='op_addsub__op_addsub__cell_18__b.F', d=0.5132154019559578)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_03__onehot00', d=1.4753600622860523)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_03__onehot00', d=1.4753600622860523)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_18__b.F'], o='op_addsub__op_addsub__cell_03__onehot01', d=1.2608044715365314)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_18__b.F'], o='op_addsub__op_addsub__cell_03__onehot01', d=1.2608044715365314)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_03__onehot10', d=1.1653563449181947)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_03__onehot10', d=1.1653563449181947)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_18__b.F', 'op_addsub__op_addsub__op.F'], o='op_addsub__op_addsub__cell_12__b.T', d=0.6571636089804004)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_18__b.F', 'op_addsub__op_addsub__op.F'], o='op_addsub__op_addsub__cell_12__b.T', d=0.6571636089804004)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_03__onehot01', 'op_addsub__op_addsub__cell_03__onehot00', 'op_addsub__op_addsub__cell_03__onehot10'], o='op_addsub__op_addsub__cell_12__b.F', d=0.864214559592652)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_03__onehot01', 'op_addsub__op_addsub__cell_03__onehot00', 'op_addsub__op_addsub__cell_03__onehot10'], o='op_addsub__op_addsub__cell_12__b.F', d=0.864214559592652)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__cell_02__onehot00'], o='op_addsub__op_addsub__cell_04__onehot00', d=0.5163250712091948)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__cell_02__onehot00'], o='op_addsub__op_addsub__cell_04__onehot00', d=0.5163250712091948)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__cell_02__onehot00'], o='op_addsub__op_addsub__cell_04__onehot01', d=0.7152175616938846)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__cell_02__onehot00'], o='op_addsub__op_addsub__cell_04__onehot01', d=0.7152175616938846)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__cell_04__a_T'], o='op_addsub__op_addsub__cell_04__onehot10', d=1.138760693954642)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__cell_04__a_T'], o='op_addsub__op_addsub__cell_04__onehot10', d=1.138760693954642)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__cell_04__a_T'], o='op_addsub__op_addsub__cell_06__a.F', d=0.6241060272273222)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__cell_04__a_T'], o='op_addsub__op_addsub__cell_06__a.F', d=0.6241060272273222)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_04__onehot00', 'op_addsub__op_addsub__cell_04__onehot10', 'op_addsub__op_addsub__cell_04__onehot01'], o='op_addsub__op_addsub__cell_06__a.T', d=1.292544319130926)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_04__onehot00', 'op_addsub__op_addsub__cell_04__onehot10', 'op_addsub__op_addsub__cell_04__onehot01'], o='op_addsub__op_addsub__cell_06__a.T', d=1.292544319130926)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_05__onehot00', d=1.4104974563982835)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_05__onehot00', d=1.4104974563982835)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_05__onehot01', d=1.0379877901414947)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__b(1).F'], o='op_addsub__op_addsub__cell_05__onehot01', d=1.0379877901414947)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_05__onehot10', d=1.385768587988812)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_05__onehot10', d=1.385768587988812)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_06__b.F', d=0.9939459980085006)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__b(1).T'], o='op_addsub__op_addsub__cell_06__b.F', d=0.9939459980085006)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_05__onehot10', 'op_addsub__op_addsub__cell_05__onehot00', 'op_addsub__op_addsub__cell_05__onehot01'], o='op_addsub__op_addsub__cell_06__b.T', d=1.4043077367415528)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_05__onehot10', 'op_addsub__op_addsub__cell_05__onehot00', 'op_addsub__op_addsub__cell_05__onehot01'], o='op_addsub__op_addsub__cell_06__b.T', d=1.4043077367415528)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_06__a.F', 'op_addsub__op_addsub__cell_06__b.F'], o='op_addsub__op_addsub__cell_06__onehot00', d=1.1388439720187264)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_06__a.F', 'op_addsub__op_addsub__cell_06__b.F'], o='op_addsub__op_addsub__cell_06__onehot00', d=1.1388439720187264)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_06__b.T', 'op_addsub__op_addsub__cell_06__a.F'], o='op_addsub__op_addsub__cell_06__onehot01', d=0.7710413084374041)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_06__b.T', 'op_addsub__op_addsub__cell_06__a.F'], o='op_addsub__op_addsub__cell_06__onehot01', d=0.7710413084374041)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_06__b.F', 'op_addsub__op_addsub__cell_06__a.T'], o='op_addsub__op_addsub__cell_06__onehot10', d=0.5978973457347669)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_06__b.F', 'op_addsub__op_addsub__cell_06__a.T'], o='op_addsub__op_addsub__cell_06__onehot10', d=0.5978973457347669)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_06__b.T', 'op_addsub__op_addsub__cell_06__a.T'], o='op_addsub__op_addsub__cell_08__b.T', d=0.8148410515112735)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_06__b.T', 'op_addsub__op_addsub__cell_06__a.T'], o='op_addsub__op_addsub__cell_08__b.T', d=0.8148410515112735)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_06__onehot01', 'op_addsub__op_addsub__cell_06__onehot10', 'op_addsub__op_addsub__cell_06__onehot00'], o='op_addsub__op_addsub__cell_08__b.F', d=0.8948087468450505)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_06__onehot01', 'op_addsub__op_addsub__cell_06__onehot10', 'op_addsub__op_addsub__cell_06__onehot00'], o='op_addsub__op_addsub__cell_08__b.F', d=0.8948087468450505)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__a(1).F', 'op_addsub__op_addsub__cell_08__b.T'], o='op_addsub__op_addsub__cell_08__onehot11', d=0.7889022146275231)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__a(1).F', 'op_addsub__op_addsub__cell_08__b.T'], o='op_addsub__op_addsub__cell_08__onehot11', d=0.7889022146275231)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_08__b.F', 'op_addsub__op_addsub__a(1).F'], o='op_addsub__op_addsub__cell_08__onehot10', d=1.3770531000816768)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_08__b.F', 'op_addsub__op_addsub__a(1).F'], o='op_addsub__op_addsub__cell_08__onehot10', d=1.3770531000816768)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__a(1).T', 'op_addsub__op_addsub__cell_08__b.T'], o='op_addsub__op_addsub__cell_08__onehot01', d=1.156113993031333)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__a(1).T', 'op_addsub__op_addsub__cell_08__b.T'], o='op_addsub__op_addsub__cell_08__onehot01', d=1.156113993031333)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__a(1).T', 'op_addsub__op_addsub__cell_08__b.F'], o='op_addsub__op_addsub__cell_08__onehot00', d=1.4695852917053374)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__a(1).T', 'op_addsub__op_addsub__cell_08__b.F'], o='op_addsub__op_addsub__cell_08__onehot00', d=1.4695852917053374)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_08__onehot01', 'op_addsub__op_addsub__cell_08__onehot11', 'op_addsub__op_addsub__cell_08__onehot10'], o='op_addsub__op_addsub__cell_11__a_T', d=1.1009771725295583)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_08__onehot01', 'op_addsub__op_addsub__cell_08__onehot11', 'op_addsub__op_addsub__cell_08__onehot10'], o='op_addsub__op_addsub__cell_11__a_T', d=1.1009771725295583)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_08__onehot01', 'op_addsub__op_addsub__cell_08__onehot10'], o='op_addsub__op_addsub__cell_10__b.T', d=1.1629739722860366)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_08__onehot01', 'op_addsub__op_addsub__cell_08__onehot10'], o='op_addsub__op_addsub__cell_10__b.T', d=1.1629739722860366)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_08__onehot11'], o='op_addsub__op_addsub__cell_10__b.F', d=1.306403459431485)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_08__onehot11'], o='op_addsub__op_addsub__cell_10__b.F', d=1.306403459431485)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_10__a_F', 'op_addsub__op_addsub__cell_10__b.F'], o='op_addsub__op_addsub__cell_10__onehot00', d=0.5723752732979785)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_10__a_F', 'op_addsub__op_addsub__cell_10__b.F'], o='op_addsub__op_addsub__cell_10__onehot00', d=0.5723752732979785)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_10__b.T', 'op_addsub__op_addsub__cell_10__a_F'], o='op_addsub__op_addsub__cell_10__onehot01', d=1.2801460417838333)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_10__b.T', 'op_addsub__op_addsub__cell_10__a_F'], o='op_addsub__op_addsub__cell_10__onehot01', d=1.2801460417838333)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_10__b.F'], o='op_addsub__op_addsub__cell_10__onehot10', d=1.1586521684015048)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_10__b.F'], o='op_addsub__op_addsub__cell_10__onehot10', d=1.1586521684015048)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_10__b.T'], o='op_addsub__op_addsub__cell_10__onehot11', d=0.6381406204661129)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_10__b.T'], o='op_addsub__op_addsub__cell_10__onehot11', d=0.6381406204661129)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_10__onehot00', 'op_addsub__op_addsub__cell_10__onehot01', 'op_addsub__op_addsub__cell_10__onehot10'], o='op_addsub__op_addsub__cell_11__b_T', d=0.726968199041313)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_10__onehot00', 'op_addsub__op_addsub__cell_10__onehot01', 'op_addsub__op_addsub__cell_10__onehot10'], o='op_addsub__op_addsub__cell_11__b_T', d=0.726968199041313)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_10__onehot01', 'op_addsub__op_addsub__cell_10__onehot10'], o='m__chA_z(1).T', d=0.7274634669167285)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_10__onehot01', 'op_addsub__op_addsub__cell_10__onehot10'], o='m__chA_z(1).T', d=0.7274634669167285)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_10__onehot00', 'op_addsub__op_addsub__cell_10__onehot11'], o='m__chA_z(1).F', d=1.320036848402426)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_10__onehot00', 'op_addsub__op_addsub__cell_10__onehot11'], o='m__chA_z(1).F', d=1.320036848402426)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_10__onehot11'], o='op_addsub__op_addsub__cell_11__onehot00', d=0.7117844775759548)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_10__onehot11'], o='op_addsub__op_addsub__cell_11__onehot00', d=0.7117844775759548)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_11__b_T'], o='op_addsub__op_addsub__cell_11__onehot01', d=0.5753443386655572)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_08__onehot00', 'op_addsub__op_addsub__cell_11__b_T'], o='op_addsub__op_addsub__cell_11__onehot01', d=0.5753443386655572)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_10__onehot11', 'op_addsub__op_addsub__cell_11__a_T'], o='op_addsub__op_addsub__cell_11__onehot10', d=1.194830305850485)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_10__onehot11', 'op_addsub__op_addsub__cell_11__a_T'], o='op_addsub__op_addsub__cell_11__onehot10', d=1.194830305850485)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_11__a_T', 'op_addsub__op_addsub__cell_11__b_T'], o='op_addsub__op_addsub__cell_16__a.F', d=1.1999737642556385)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_11__a_T', 'op_addsub__op_addsub__cell_11__b_T'], o='op_addsub__op_addsub__cell_16__a.F', d=1.1999737642556385)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_11__onehot00', 'op_addsub__op_addsub__cell_11__onehot10', 'op_addsub__op_addsub__cell_11__onehot01'], o='op_addsub__op_addsub__cell_16__a.T', d=0.5800564432856269)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_11__onehot00', 'op_addsub__op_addsub__cell_11__onehot10', 'op_addsub__op_addsub__cell_11__onehot01'], o='op_addsub__op_addsub__cell_16__a.T', d=0.5800564432856269)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_12__b.F'], o='op_addsub__op_addsub__cell_12__onehot00', d=1.4919534218711155)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_12__b.F'], o='op_addsub__op_addsub__cell_12__onehot00', d=1.4919534218711155)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_12__b.T'], o='op_addsub__op_addsub__cell_12__onehot01', d=0.804411220429004)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_12__b.T'], o='op_addsub__op_addsub__cell_12__onehot01', d=0.804411220429004)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_12__onehot10', d=0.6031075269998076)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.F', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_12__onehot10', d=0.6031075269998076)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_12__onehot11', d=0.9041172389619128)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_12__b.T', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_12__onehot11', d=0.9041172389619128)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_12__onehot01', 'op_addsub__op_addsub__cell_12__onehot10'], o='op_addsub__op_addsub__cell_14__b.T', d=1.064109799060553)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_12__onehot01', 'op_addsub__op_addsub__cell_12__onehot10'], o='op_addsub__op_addsub__cell_14__b.T', d=1.064109799060553)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_12__onehot11', 'op_addsub__op_addsub__cell_12__onehot00'], o='op_addsub__op_addsub__cell_14__b.F', d=1.1646456124147941)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_12__onehot11', 'op_addsub__op_addsub__cell_12__onehot00'], o='op_addsub__op_addsub__cell_14__b.F', d=1.1646456124147941)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_14__b.F', 'op_addsub__op_addsub__a(2).F'], o='op_addsub__op_addsub__cell_14__onehot00', d=1.4573964208631636)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_14__b.F', 'op_addsub__op_addsub__a(2).F'], o='op_addsub__op_addsub__cell_14__onehot00', d=1.4573964208631636)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_14__b.T', 'op_addsub__op_addsub__a(2).F'], o='op_addsub__op_addsub__cell_14__onehot01', d=1.439693860494109)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_14__b.T', 'op_addsub__op_addsub__a(2).F'], o='op_addsub__op_addsub__cell_14__onehot01', d=1.439693860494109)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_14__b.F', 'op_addsub__op_addsub__a(2).T'], o='op_addsub__op_addsub__cell_14__onehot10', d=0.5270429024101373)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_14__b.F', 'op_addsub__op_addsub__a(2).T'], o='op_addsub__op_addsub__cell_14__onehot10', d=0.5270429024101373)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_14__b.T', 'op_addsub__op_addsub__a(2).T'], o='op_addsub__op_addsub__cell_14__onehot11', d=0.6716141783655626)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_14__b.T', 'op_addsub__op_addsub__a(2).T'], o='op_addsub__op_addsub__cell_14__onehot11', d=0.6716141783655626)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_14__onehot10', 'op_addsub__op_addsub__cell_14__onehot01', 'op_addsub__op_addsub__cell_14__onehot00'], o='op_addsub__op_addsub__cell_17__a_T', d=0.7005412220442634)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_14__onehot10', 'op_addsub__op_addsub__cell_14__onehot01', 'op_addsub__op_addsub__cell_14__onehot00'], o='op_addsub__op_addsub__cell_17__a_T', d=0.7005412220442634)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_14__onehot10', 'op_addsub__op_addsub__cell_14__onehot01'], o='op_addsub__op_addsub__cell_16__b.T', d=0.838880441311951)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_14__onehot10', 'op_addsub__op_addsub__cell_14__onehot01'], o='op_addsub__op_addsub__cell_16__b.T', d=0.838880441311951)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_14__onehot00', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_16__b.F', d=1.366569687555054)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_14__onehot00', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_16__b.F', d=1.366569687555054)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__a.F', 'op_addsub__op_addsub__cell_16__b.F'], o='op_addsub__op_addsub__cell_16__onehot00', d=1.3033461034508933)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__a.F', 'op_addsub__op_addsub__cell_16__b.F'], o='op_addsub__op_addsub__cell_16__onehot00', d=1.3033461034508933)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__a.F', 'op_addsub__op_addsub__cell_16__b.T'], o='op_addsub__op_addsub__cell_16__onehot01', d=0.6793311021217491)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__a.F', 'op_addsub__op_addsub__cell_16__b.T'], o='op_addsub__op_addsub__cell_16__onehot01', d=0.6793311021217491)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__b.F', 'op_addsub__op_addsub__cell_16__a.T'], o='op_addsub__op_addsub__cell_16__onehot10', d=0.8201747992478226)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__b.F', 'op_addsub__op_addsub__cell_16__a.T'], o='op_addsub__op_addsub__cell_16__onehot10', d=0.8201747992478226)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__a.T', 'op_addsub__op_addsub__cell_16__b.T'], o='op_addsub__op_addsub__cell_16__onehot11', d=0.5714656043075453)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__a.T', 'op_addsub__op_addsub__cell_16__b.T'], o='op_addsub__op_addsub__cell_16__onehot11', d=0.5714656043075453)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_16__onehot01', 'op_addsub__op_addsub__cell_16__onehot00', 'op_addsub__op_addsub__cell_16__onehot10'], o='op_addsub__op_addsub__cell_17__b_T', d=0.7445399499056734)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_16__onehot01', 'op_addsub__op_addsub__cell_16__onehot00', 'op_addsub__op_addsub__cell_16__onehot10'], o='op_addsub__op_addsub__cell_17__b_T', d=0.7445399499056734)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_16__onehot01', 'op_addsub__op_addsub__cell_16__onehot10'], o='m__chA_z(2).T', d=0.7841333362550803)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_16__onehot01', 'op_addsub__op_addsub__cell_16__onehot10'], o='m__chA_z(2).T', d=0.7841333362550803)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_16__onehot00'], o='m__chA_z(2).F', d=0.7937621472032244)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_16__onehot00'], o='m__chA_z(2).F', d=0.7937621472032244)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_17__onehot00', d=0.8419597049591616)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_17__onehot00', d=0.8419597049591616)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_17__b_T', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_17__onehot01', d=0.5333515958361374)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_17__b_T', 'op_addsub__op_addsub__cell_14__onehot11'], o='op_addsub__op_addsub__cell_17__onehot01', d=0.5333515958361374)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_17__a_T'], o='op_addsub__op_addsub__cell_17__onehot10', d=1.0061858087719906)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_16__onehot11', 'op_addsub__op_addsub__cell_17__a_T'], o='op_addsub__op_addsub__cell_17__onehot10', d=1.0061858087719906)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_17__a_T', 'op_addsub__op_addsub__cell_17__b_T'], o='op_addsub__op_addsub__cell_22__a.T', d=1.3478524470895739)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_17__a_T', 'op_addsub__op_addsub__cell_17__b_T'], o='op_addsub__op_addsub__cell_22__a.T', d=1.3478524470895739)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_17__onehot10', 'op_addsub__op_addsub__cell_17__onehot00', 'op_addsub__op_addsub__cell_17__onehot01'], o='op_addsub__op_addsub__cell_22__a.F', d=0.7880139759367188)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_17__onehot10', 'op_addsub__op_addsub__cell_17__onehot00', 'op_addsub__op_addsub__cell_17__onehot01'], o='op_addsub__op_addsub__cell_22__a.F', d=0.7880139759367188)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_18__b.F', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_18__onehot00', d=0.510267543351972)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_18__b.F', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_18__onehot00', d=0.510267543351972)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_18__b.T', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_18__onehot01', d=1.014837305002719)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_18__b.T', 'op_addsub__op_addsub__b(2).T'], o='op_addsub__op_addsub__cell_18__onehot01', d=1.014837305002719)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_18__b.F'], o='op_addsub__op_addsub__cell_18__onehot10', d=1.030308338374325)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_18__b.F'], o='op_addsub__op_addsub__cell_18__onehot10', d=1.030308338374325)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_19__b.F', d=0.8400422977345852)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(2).F', 'op_addsub__op_addsub__cell_18__b.T'], o='op_addsub__op_addsub__cell_19__b.F', d=0.8400422977345852)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_18__onehot01', 'op_addsub__op_addsub__cell_18__onehot10', 'op_addsub__op_addsub__cell_18__onehot00'], o='op_addsub__op_addsub__cell_19__b.T', d=0.672054449760264)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_18__onehot01', 'op_addsub__op_addsub__cell_18__onehot10', 'op_addsub__op_addsub__cell_18__onehot00'], o='op_addsub__op_addsub__cell_19__b.T', d=0.672054449760264)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_19__b.F'], o='op_addsub__op_addsub__cell_19__onehot00', d=1.1430766248258954)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_19__b.F'], o='op_addsub__op_addsub__cell_19__onehot00', d=1.1430766248258954)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_19__b.T'], o='op_addsub__op_addsub__cell_19__onehot01', d=0.5916407354450455)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.T', 'op_addsub__op_addsub__cell_19__b.T'], o='op_addsub__op_addsub__cell_19__onehot01', d=0.5916407354450455)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__cell_19__b.F'], o='op_addsub__op_addsub__cell_19__onehot10', d=1.0686658762000243)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__op.F', 'op_addsub__op_addsub__cell_19__b.F'], o='op_addsub__op_addsub__cell_19__onehot10', d=1.0686658762000243)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_19__b.T', 'op_addsub__op_addsub__op.F'], o='op_addsub__op_addsub__cell_21__a.T', d=1.1425078749241415)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_19__b.T', 'op_addsub__op_addsub__op.F'], o='op_addsub__op_addsub__cell_21__a.T', d=1.1425078749241415)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_19__onehot10', 'op_addsub__op_addsub__cell_19__onehot00', 'op_addsub__op_addsub__cell_19__onehot01'], o='op_addsub__op_addsub__cell_21__a.F', d=1.4469891575463452)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_19__onehot10', 'op_addsub__op_addsub__cell_19__onehot00', 'op_addsub__op_addsub__cell_19__onehot01'], o='op_addsub__op_addsub__cell_21__a.F', d=1.4469891575463452)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(3).T', 'op_addsub__op_addsub__a(3).F'], o='op_addsub__op_addsub__cell_20__onehot00', d=1.3782959649444013)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(3).T', 'op_addsub__op_addsub__a(3).F'], o='op_addsub__op_addsub__cell_20__onehot00', d=1.3782959649444013)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(3).T', 'op_addsub__op_addsub__a(3).T'], o='op_addsub__op_addsub__cell_20__onehot01', d=1.4281766620497522)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(3).T', 'op_addsub__op_addsub__a(3).T'], o='op_addsub__op_addsub__cell_20__onehot01', d=1.4281766620497522)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(3).F', 'op_addsub__op_addsub__a(3).F'], o='op_addsub__op_addsub__cell_20__onehot10', d=0.6743453119003701)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(3).F', 'op_addsub__op_addsub__a(3).F'], o='op_addsub__op_addsub__cell_20__onehot10', d=0.6743453119003701)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__b(3).F', 'op_addsub__op_addsub__a(3).T'], o='op_addsub__op_addsub__cell_20__onehot11', d=0.5131813139206621)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__b(3).F', 'op_addsub__op_addsub__a(3).T'], o='op_addsub__op_addsub__cell_20__onehot11', d=0.5131813139206621)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_20__onehot01', 'op_addsub__op_addsub__cell_20__onehot10'], o='op_addsub__op_addsub__cell_21__b.T', d=1.3038250750242604)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_20__onehot01', 'op_addsub__op_addsub__cell_20__onehot10'], o='op_addsub__op_addsub__cell_21__b.T', d=1.3038250750242604)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_20__onehot11', 'op_addsub__op_addsub__cell_20__onehot00'], o='op_addsub__op_addsub__cell_21__b.F', d=1.364254072956479)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_20__onehot11', 'op_addsub__op_addsub__cell_20__onehot00'], o='op_addsub__op_addsub__cell_21__b.F', d=1.364254072956479)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_21__b.F', 'op_addsub__op_addsub__cell_21__a.F'], o='op_addsub__op_addsub__cell_21__onehot00', d=1.0441204588818316)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_21__b.F', 'op_addsub__op_addsub__cell_21__a.F'], o='op_addsub__op_addsub__cell_21__onehot00', d=1.0441204588818316)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_21__b.T', 'op_addsub__op_addsub__cell_21__a.F'], o='op_addsub__op_addsub__cell_21__onehot01', d=1.3316473108564055)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_21__b.T', 'op_addsub__op_addsub__cell_21__a.F'], o='op_addsub__op_addsub__cell_21__onehot01', d=1.3316473108564055)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_21__b.F', 'op_addsub__op_addsub__cell_21__a.T'], o='op_addsub__op_addsub__cell_21__onehot10', d=1.3746444539561105)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_21__b.F', 'op_addsub__op_addsub__cell_21__a.T'], o='op_addsub__op_addsub__cell_21__onehot10', d=1.3746444539561105)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_21__b.T', 'op_addsub__op_addsub__cell_21__a.T'], o='op_addsub__op_addsub__cell_21__onehot11', d=1.1099901669784409)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_21__b.T', 'op_addsub__op_addsub__cell_21__a.T'], o='op_addsub__op_addsub__cell_21__onehot11', d=1.1099901669784409)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_21__onehot01', 'op_addsub__op_addsub__cell_21__onehot10'], o='op_addsub__op_addsub__cell_22__b.T', d=1.3945194492524569)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_21__onehot01', 'op_addsub__op_addsub__cell_21__onehot10'], o='op_addsub__op_addsub__cell_22__b.T', d=1.3945194492524569)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_21__onehot00', 'op_addsub__op_addsub__cell_21__onehot11'], o='op_addsub__op_addsub__cell_22__b.F', d=0.9647820878772574)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_21__onehot00', 'op_addsub__op_addsub__cell_21__onehot11'], o='op_addsub__op_addsub__cell_22__b.F', d=0.9647820878772574)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_22__b.F', 'op_addsub__op_addsub__cell_22__a.F'], o='op_addsub__op_addsub__cell_22__onehot00', d=1.270385121257688)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_22__b.F', 'op_addsub__op_addsub__cell_22__a.F'], o='op_addsub__op_addsub__cell_22__onehot00', d=1.270385121257688)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_22__a.F', 'op_addsub__op_addsub__cell_22__b.T'], o='op_addsub__op_addsub__cell_22__onehot01', d=1.400573307663489)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_22__a.F', 'op_addsub__op_addsub__cell_22__b.T'], o='op_addsub__op_addsub__cell_22__onehot01', d=1.400573307663489)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_22__b.F', 'op_addsub__op_addsub__cell_22__a.T'], o='op_addsub__op_addsub__cell_22__onehot10', d=1.4214921835170087)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_22__b.F', 'op_addsub__op_addsub__cell_22__a.T'], o='op_addsub__op_addsub__cell_22__onehot10', d=1.4214921835170087)

	tr.rise(f=tr.Cr, i=['op_addsub__op_addsub__cell_22__b.T', 'op_addsub__op_addsub__cell_22__a.T'], o='op_addsub__op_addsub__cell_22__onehot11', d=1.1310988567696363)
	tr.fall(f=tr.Cf, i=['op_addsub__op_addsub__cell_22__b.T', 'op_addsub__op_addsub__cell_22__a.T'], o='op_addsub__op_addsub__cell_22__onehot11', d=1.1310988567696363)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_22__onehot10', 'op_addsub__op_addsub__cell_22__onehot01'], o='m__chA_z(3).T', d=0.5690160267498656)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_22__onehot10', 'op_addsub__op_addsub__cell_22__onehot01'], o='m__chA_z(3).T', d=0.5690160267498656)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_22__onehot00', 'op_addsub__op_addsub__cell_22__onehot11'], o='m__chA_z(3).F', d=1.3164293140801373)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_22__onehot00', 'op_addsub__op_addsub__cell_22__onehot11'], o='m__chA_z(3).F', d=1.3164293140801373)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_23__onehot10', 'op_addsub__op_addsub__cell_23__onehot01'], o='m__chA_z(0).T', d=0.6748928267733019)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_23__onehot10', 'op_addsub__op_addsub__cell_23__onehot01'], o='m__chA_z(0).T', d=0.6748928267733019)

	tr.rise(f=tr.ORr, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_23__onehot00'], o='m__chA_z(0).F', d=1.1458572914502994)
	tr.fall(f=tr.ORf, i=['op_addsub__op_addsub__cell_23__onehot11', 'op_addsub__op_addsub__cell_23__onehot00'], o='m__chA_z(0).F', d=1.1458572914502994)

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
