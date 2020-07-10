#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @Author :  Chris Sun
 @Email  :  sunkepeng@hisense.com
 @DateTime : 2020/2/22-15:45
 @Description : database style for the project
"""

from HisenseTest import db
from flask_login import UserMixin


class User(UserMixin):
    pass


users = [
    {
        'id': 'hisense',
        'username': 'hisense',
        'password': 'hisense'
    }
]


def query_user(user_id):
    for user in users:
        return user


class Testdata(db.Model):
    __tablename__ = 'autotestdata'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    MachineID = db.Column(db.String(32), unique=True)
    Mac = db.Column(db.String(32))
    Widevine = db.Column(db.String(32))
    ChinaDrm = db.Column(db.String(32))
    Hdcp = db.Column(db.String(32))
    ATV_Synchrolock = db.Column(db.String(32))
    ATV_FieldRate = db.Column(db.String(32))
    ATV_ImageFormat = db.Column(db.String(32))
    ATV_SoundFormat = db.Column(db.String(32))
    ATV_NoiseIntensity = db.Column(db.String(32))
    ATV_Final = db.Column(db.String(32))
    DTMB_Synchrolock = db.Column(db.String(32))
    DTMB_ImageFormat = db.Column(db.String(32))
    DTMB_SignalStrength = db.Column(db.String(32))
    DTMB_Final = db.Column(db.String(32))
    DVBC_Synchrolock = db.Column(db.String(32))
    DVBC_ImageFormat = db.Column(db.String(32))
    DVBC_SignalStrength = db.Column(db.String(32))
    DVBC_Final = db.Column(db.String(32))
    AV_FieldRate = db.Column(db.String(32))
    AV_ImageFormat = db.Column(db.String(32))
    AV_Final = db.Column(db.String(32))
    HDMI1_FieldRate = db.Column(db.String(32))
    HDMI1_Distinguish = db.Column(db.String(32))
    HDMI1_ConnectState = db.Column(db.String(32))
    HDMI1_HdmiState = db.Column(db.String(32))
    HDMI1_HdcpState = db.Column(db.String(32))
    HDMI1_Final = db.Column(db.String(32))
    HDMI2_FieldRate = db.Column(db.String(32))
    HDMI2_Distinguish = db.Column(db.String(32))
    HDMI2_ConnectState = db.Column(db.String(32))
    HDMI2_HdmiState = db.Column(db.String(32))
    HDMI2_HdcpState = db.Column(db.String(32))
    HDMI2_Final = db.Column(db.String(32))
    SourceImage = db.Column(db.String(32))
    WifiConnection = db.Column(db.String(32))
    BT_Driver = db.Column(db.String(32))
    BT_Enable = db.Column(db.String(32))
    BT_RF = db.Column(db.String(32))
    ScreenTest = db.Column(db.String(32))
    Saving = db.Column(db.String(32))
    MIC = db.Column(db.String(32))
    Vcom = db.Column(db.String(32))
    WB = db.Column(db.String(32))


    def __init__(self, MachineID, Mac, Widevine, ChinaDrm, Hdcp, ATV_Synchrolock, ATV_FieldRate, ATV_ImageFormat,
                 ATV_SoundFormat, ATV_NoiseIntensity, ATV_Final, DTMB_Synchrolock, DTMB_ImageFormat,
                 DTMB_SignalStrength, DTMB_Final, DVBC_Synchrolock, DVBC_ImageFormat, DVBC_SignalStrength, DVBC_Final,
                 AV_FieldRate, AV_ImageFormat, AV_Final, HDMI1_FieldRate, HDMI1_Distinguish, HDMI1_ConnectState,
                 HDMI1_HdmiState, HDMI1_HdcpState, HDMI1_Final, HDMI2_FieldRate, HDMI2_Distinguish, HDMI2_ConnectState,
                 HDMI2_HdmiState, HDMI2_HdcpState, HDMI2_Final, SourceImage, WifiConnection, BT_Driver, BT_Enable, BT_RF,
                 ScreenTest, Saving, MIC, Vcom, WB):
        self.MachineID = MachineID
        self.Mac = Mac
        self.Widevine = Widevine
        self.ChinaDrm = ChinaDrm
        self.Hdcp = Hdcp
        self.ATV_Synchrolock = ATV_Synchrolock
        self.ATV_FieldRate = ATV_FieldRate
        self.ATV_ImageFormat = ATV_ImageFormat
        self.ATV_SoundFormat = ATV_SoundFormat
        self.ATV_NoiseIntensity = ATV_NoiseIntensity
        self.ATV_Final = ATV_Final
        self.DTMB_Synchrolock = DTMB_Synchrolock
        self.DTMB_ImageFormat = DTMB_ImageFormat
        self.DTMB_SignalStrength = DTMB_SignalStrength
        self.DTMB_Final = DTMB_Final
        self.DVBC_Synchrolock = DVBC_Synchrolock
        self.DVBC_ImageFormat = DVBC_ImageFormat
        self.DVBC_SignalStrength = DVBC_SignalStrength
        self.DVBC_Final = DVBC_Final
        self.AV_FieldRate = AV_FieldRate
        self.AV_ImageFormat = AV_ImageFormat
        self.AV_Final = AV_Final
        self.HDMI1_FieldRate = HDMI1_FieldRate
        self.HDMI1_Distinguish = HDMI1_Distinguish
        self.HDMI1_ConnectState = HDMI1_ConnectState
        self.HDMI1_HdmiState = HDMI1_HdmiState
        self.HDMI1_HdcpState = HDMI1_HdcpState
        self.HDMI1_Final = HDMI1_Final
        self.HDMI2_FieldRate = HDMI2_FieldRate
        self.HDMI2_Distinguish = HDMI2_Distinguish
        self.HDMI2_ConnectState = HDMI2_ConnectState
        self.HDMI2_HdmiState = HDMI2_HdmiState
        self.HDMI2_HdcpState = HDMI2_HdcpState
        self.HDMI2_Final = HDMI2_Final
        self.SourceImage = SourceImage
        self.WifiConnection = WifiConnection
        self.BT_Driver = BT_Driver
        self.BT_Enable = BT_Enable
        self.BT_RF = BT_RF
        self.ScreenTest = ScreenTest
        self.Saving = Saving
        self.MIC = MIC
        self.Vcom = Vcom
        self.WB = WB

    def __repr__(self):
        return '%d %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' \
               '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' \
               '%s %s %s %s %s %s %s %s %s' % (self.id, self.MachineID, self.Mac, self.Widevine, self.ChinaDrm,
                                               self.Hdcp, self.ATV_Synchrolock, self.ATV_FieldRate,
                                               self.ATV_ImageFormat, self.ATV_SoundFormat,
                                               self.ATV_NoiseIntensity, self.ATV_Final, self.DTMB_Synchrolock,
                                               self.DTMB_ImageFormat,
                                               self.DTMB_SignalStrength, self.DTMB_Final, self.DVBC_Synchrolock,
                                               self.DVBC_ImageFormat, self.DVBC_SignalStrength,
                                               self.DVBC_Final, self.AV_FieldRate, self.AV_ImageFormat, self.AV_Final,
                                               self.HDMI1_FieldRate,
                                               self.HDMI1_Distinguish, self.HDMI1_ConnectState, self.HDMI1_HdmiState,
                                               self.HDMI1_HdcpState, self.HDMI1_Final,
                                               self.HDMI2_FieldRate, self.HDMI2_Distinguish, self.HDMI2_ConnectState,
                                               self.HDMI2_HdmiState, self.HDMI2_HdcpState,
                                               self.HDMI2_Final, self.SourceImage, self.WifiConnection, self.BT_Driver,
                                               self.BT_Enable,
                                               self.BT_RF, self.ScreenTest, self.Saving, self.MIC, self.Vcom, self.WB)
