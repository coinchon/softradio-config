#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: DAB VHF Baseband Player for UHD (USRP)
# Author: Mathias Coinchon
# Description: DAB VHF Baseband Player for UHD (USRP)
# Generated: Fri Dec 13 14:14:45 2013
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.fft import window
from gnuradio.filter import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class coinwap_uhd_full3(grc_wxgui.top_block_gui):

    def __init__(self, subdev="A:0", frequency=216928000, ant="TX/RX", gain=10, enable_filter=0, rate=3.2e6, devid="type=b100"):
        grc_wxgui.top_block_gui.__init__(self, title="DAB VHF Baseband Player for UHD (USRP)")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Parameters
        ##################################################
        self.subdev = subdev
        self.frequency = frequency
        self.ant = ant
        self.gain = gain
        self.enable_filter = enable_filter
        self.rate = rate
        self.devid = devid

        ##################################################
        # Variables
        ##################################################
        self.transition0 = transition0 = 150000
        self.switch2 = switch2 = 1
        self.switch1 = switch1 = enable_filter
        self.switch0 = switch0 = False
        self.samp_rate = samp_rate = int(rate)
        self.gain0 = gain0 = gain
        self.frequency0 = frequency0 = frequency
        self.dgain = dgain = 1.0/32768
        self.cutoff0 = cutoff0 = 810000

        ##################################################
        # Blocks
        ##################################################
        _transition0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._transition0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_transition0_sizer,
        	value=self.transition0,
        	callback=self.set_transition0,
        	label="Transition frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._transition0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_transition0_sizer,
        	value=self.transition0,
        	callback=self.set_transition0,
        	minimum=100,
        	maximum=1000000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_transition0_sizer, 6, 0, 1, 20)
        self._switch2_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.switch2,
        	callback=self.set_switch2,
        	label="Spectrum display mute",
        	true=1,
        	false=0,
        )
        self.GridAdd(self._switch2_check_box, 3, 0, 1, 1)
        self._switch1_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.switch1,
        	callback=self.set_switch1,
        	label="Filter",
        	true=1,
        	false=0,
        )
        self.GridAdd(self._switch1_check_box, 4, 0, 1, 1)
        self._switch0_check_box = forms.check_box(
        	parent=self.GetWin(),
        	value=self.switch0,
        	callback=self.set_switch0,
        	label="Clean carrier (Modulator Off)",
        	true=1.0,
        	false=0,
        )
        self.GridAdd(self._switch0_check_box, 2, 0, 1, 1)
        _gain0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._gain0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_gain0_sizer,
        	value=self.gain0,
        	callback=self.set_gain0,
        	label="Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._gain0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_gain0_sizer,
        	value=self.gain0,
        	callback=self.set_gain0,
        	minimum=0,
        	maximum=20,
        	num_steps=40,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_gain0_sizer, 1, 0, 1, 20)
        self._frequency0_chooser = forms.drop_down(
        	parent=self.GetWin(),
        	value=self.frequency0,
        	callback=self.set_frequency0,
        	label="Channel frequency",
        	choices=[174928000, 176640000, 178352000, 180064000, 181936000, 183648000, 185360000, 187072000, 188928000, 190640000, 192352000, 194064000, 195936000, 197648000, 199360000, 201072000, 202928000, 204640000, 206352000, 208064000, 209936000, 211648000, 213360000, 215072000, 216928000, 218640000, 220352000, 222064000, 223936000, 225648000, 227360000, 229072000, 230784000, 232496000, 234208000, 235776000, 237488000, 239200000],
        	labels=["5A", "5B", "5C", "5D", "6A", "6B", "6C", "6D", "7A", "7B", "7C", "7D", "8A", "8B", "8C", "8D", "9A", "9B", "9C", "9D", "10A", "10B", "10C", "10D", "11A", "11B", "11C", "11D", "12A", "12B", "12C", "12D", "13A", "13B", "13C", "13D", "13E", "13F"],
        )
        self.GridAdd(self._frequency0_chooser, 0, 0, 1, 1)
        _dgain_sizer = wx.BoxSizer(wx.VERTICAL)
        self._dgain_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_dgain_sizer,
        	value=self.dgain,
        	callback=self.set_dgain,
        	label="Digital Gain",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._dgain_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_dgain_sizer,
        	value=self.dgain,
        	callback=self.set_dgain,
        	minimum=0,
        	maximum=1.0/10000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_dgain_sizer, 7, 0, 1, 20)
        _cutoff0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._cutoff0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_cutoff0_sizer,
        	value=self.cutoff0,
        	callback=self.set_cutoff0,
        	label="Cutoff Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._cutoff0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_cutoff0_sizer,
        	value=self.cutoff0,
        	callback=self.set_cutoff0,
        	minimum=1,
        	maximum=1500000,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_cutoff0_sizer, 5, 0, 1, 20)
        self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
        	self.GetWin(),
        	baseband_freq=0,
        	y_per_div=5,
        	y_divs=15,
        	ref_level=60,
        	ref_scale=2.0,
        	sample_rate=samp_rate,
        	fft_size=1024,
        	fft_rate=5,
        	average=True,
        	avg_alpha=None,
        	title="FFT Plot",
        	peak_hold=False,
        )
        self.Add(self.wxgui_fftsink2_0.win)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	device_addr=devid,
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_subdev_spec(subdev, 0)
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(frequency0, 0)
        self.uhd_usrp_sink_0.set_gain(gain0, 0)
        self.uhd_usrp_sink_0.set_antenna(ant, 0)
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, cutoff0, transition0, firdes.WIN_HAMMING, 6.76))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((dgain, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/dev/stdin", False)
        self.blks2_valve_1_0 = grc_blks2.valve(item_size=gr.sizeof_gr_complex*1, open=bool(switch0))
        self.blks2_valve_1 = grc_blks2.valve(item_size=gr.sizeof_gr_complex*1, open=bool(switch2))
        self.blks2_selector_1 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=switch1,
        	output_index=0,
        )
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=1,
        	num_outputs=2,
        	input_index=0,
        	output_index=switch1,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_valve_1, 0), (self.wxgui_fftsink2_0, 0))
        self.connect((self.blks2_selector_1, 0), (self.blks2_valve_1, 0))
        self.connect((self.low_pass_filter_0, 0), (self.blks2_selector_1, 1))
        self.connect((self.blks2_selector_0, 0), (self.blks2_selector_1, 0))
        self.connect((self.blks2_selector_0, 1), (self.low_pass_filter_0, 0))
        self.connect((self.blks2_selector_1, 0), (self.blks2_valve_1_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.blks2_valve_1_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.uhd_usrp_sink_0, 0))


# QT sink close method reimplementation

    def get_subdev(self):
        return self.subdev

    def set_subdev(self, subdev):
        self.subdev = subdev

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.set_frequency0(self.frequency)

    def get_ant(self):
        return self.ant

    def set_ant(self, ant):
        self.ant = ant
        self.uhd_usrp_sink_0.set_antenna(self.ant, 0)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.set_gain0(self.gain)

    def get_enable_filter(self):
        return self.enable_filter

    def set_enable_filter(self, enable_filter):
        self.enable_filter = enable_filter
        self.set_switch1(self.enable_filter)

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate
        self.set_samp_rate(int(self.rate))

    def get_devid(self):
        return self.devid

    def set_devid(self, devid):
        self.devid = devid

    def get_transition0(self):
        return self.transition0

    def set_transition0(self, transition0):
        self.transition0 = transition0
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff0, self.transition0, firdes.WIN_HAMMING, 6.76))
        self._transition0_slider.set_value(self.transition0)
        self._transition0_text_box.set_value(self.transition0)

    def get_switch2(self):
        return self.switch2

    def set_switch2(self, switch2):
        self.switch2 = switch2
        self.blks2_valve_1.set_open(bool(self.switch2))
        self._switch2_check_box.set_value(self.switch2)

    def get_switch1(self):
        return self.switch1

    def set_switch1(self, switch1):
        self.switch1 = switch1
        self.blks2_selector_1.set_input_index(int(self.switch1))
        self._switch1_check_box.set_value(self.switch1)
        self.blks2_selector_0.set_output_index(int(self.switch1))

    def get_switch0(self):
        return self.switch0

    def set_switch0(self, switch0):
        self.switch0 = switch0
        self._switch0_check_box.set_value(self.switch0)
        self.blks2_valve_1_0.set_open(bool(self.switch0))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff0, self.transition0, firdes.WIN_HAMMING, 6.76))
        self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_gain0(self):
        return self.gain0

    def set_gain0(self, gain0):
        self.gain0 = gain0
        self._gain0_slider.set_value(self.gain0)
        self._gain0_text_box.set_value(self.gain0)
        self.uhd_usrp_sink_0.set_gain(self.gain0, 0)

    def get_frequency0(self):
        return self.frequency0

    def set_frequency0(self, frequency0):
        self.frequency0 = frequency0
        self._frequency0_chooser.set_value(self.frequency0)
        self.uhd_usrp_sink_0.set_center_freq(self.frequency0, 0)

    def get_dgain(self):
        return self.dgain

    def set_dgain(self, dgain):
        self.dgain = dgain
        self.blocks_multiply_const_vxx_0.set_k((self.dgain, ))
        self._dgain_slider.set_value(self.dgain)
        self._dgain_text_box.set_value(self.dgain)

    def get_cutoff0(self):
        return self.cutoff0

    def set_cutoff0(self, cutoff0):
        self.cutoff0 = cutoff0
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.cutoff0, self.transition0, firdes.WIN_HAMMING, 6.76))
        self._cutoff0_slider.set_value(self.cutoff0)
        self._cutoff0_text_box.set_value(self.cutoff0)

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--subdev", dest="subdev", type="string", default="A:0",
        help="Set UHD Subdevice Name [default=%default]")
    parser.add_option("-f", "--frequency", dest="frequency", type="intx", default=216928000,
        help="Set frequency [default=%default]")
    parser.add_option("", "--ant", dest="ant", type="string", default="TX/RX",
        help="Set Antennna Port Name [default=%default]")
    parser.add_option("-g", "--gain", dest="gain", type="intx", default=10,
        help="Set TX gain (daughterboard) [default=%default]")
    parser.add_option("", "--enable-filter", dest="enable_filter", type="intx", default=0,
        help="Set Enable postfilter [default=%default]")
    parser.add_option("-r", "--rate", dest="rate", type="eng_float", default=eng_notation.num_to_str(3.2e6),
        help="Set Sample Rate for USRP [default=%default]")
    parser.add_option("-a", "--devid", dest="devid", type="string", default="type=b100",
        help="Set device id [default=%default]")
    (options, args) = parser.parse_args()
    if gr.enable_realtime_scheduling() != gr.RT_OK:
        print "Error: failed to enable realtime scheduling."
    tb = coinwap_uhd_full3(subdev=options.subdev, frequency=options.frequency, ant=options.ant, gain=options.gain, enable_filter=options.enable_filter, rate=options.rate, devid=options.devid)
    tb.Start(True)
    tb.Wait()

