#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""
 @Author :  Chris Sun
 @Email  :  sunkepeng@hisense.com
 @DateTime : 2020/2/22-15:25
 @Description :view for the project
"""

from HisenseTest import app, db, login_manager
from HisenseTest.page_utils import Pagination
from models import User, query_user, Testdata
from flask import render_template, redirect, request, flash
from flask_login import login_user, logout_user, login_required
import json


@login_manager.user_loader
def load_user(user_id):
    if query_user(user_id) is not None:
        current_user = User()
        current_user.id = user_id
        return current_user


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userid')
        user = query_user(user_id)
        if user is not None and request.form['password'] == user['password']:
            current_user = User()
            current_user.id = user_id
            login_user(current_user)
            return redirect('/')
    return render_template('login.html')


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return render_template('login.html')


@app.errorhandler(404)
def miss(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error(e):
    return render_template('500.html'), 500


@app.route('/')
@login_required
def index():
    testdata = Testdata.query.order_by(db.desc(Testdata.id)).all()
    li = []
    for i in testdata:
        li.append(i)
    page_obj = Pagination(request.args.get("page", 1), len(li), request.path, request.args, per_page_count=23)
    index_list = li[page_obj.start: page_obj.end]
    page_html = page_obj.page_html()
    return render_template("index.html", testdata=testdata, index_list=index_list, page_html=page_html)


@app.route('/addtestdata/', methods=['POST'])
def add_testdata():
    recv_null = {}
    recv_data = request.get_data()
    recv_data = json.loads(recv_data)
    if recv_data:
        recv_ok = {}

        MachineID = recv_data['MachineID']
        Mac = recv_data['Mac']
        Widevine = recv_data['Widevine']
        ChinaDrm = recv_data['ChinaDrm']
        Hdcp = recv_data['Hdcp']
        ATV_Synchrolock = recv_data['ATV_Synchrolock']
        ATV_FieldRate = recv_data['ATV_FieldRate']
        ATV_ImageFormat = recv_data['ATV_ImageFormat']
        ATV_SoundFormat = recv_data['ATV_SoundFormat']
        ATV_NoiseIntensity = recv_data['ATV_NoiseIntensity']
        ATV_Final = recv_data['ATV_Final']
        DTMB_Synchrolock = recv_data['DTMB_Synchrolock']
        DTMB_ImageFormat = recv_data['DTMB_ImageFormat']
        DTMB_SignalStrength = recv_data['DTMB_SignalStrength']
        DTMB_Final = recv_data['DTMB_Final']
        DVBC_Synchrolock = recv_data['DVBC_Synchrolock']
        DVBC_ImageFormat = recv_data['DVBC_ImageFormat']
        DVBC_SignalStrength = recv_data['DVBC_SignalStrength']
        DVBC_Final = recv_data['DVBC_Final']
        AV_FieldRate = recv_data['AV_FieldRate']
        AV_ImageFormat = recv_data['AV_ImageFormat']
        AV_Final = recv_data['AV_Final']
        HDMI1_FieldRate = recv_data['HDMI1_FieldRate']
        HDMI1_Distinguish = recv_data['HDMI1_Distinguish']
        HDMI1_ConnectState = recv_data['HDMI1_ConnectState']
        HDMI1_HdmiState = recv_data['HDMI1_HdmiState']
        HDMI1_HdcpState = recv_data['HDMI1_HdcpState']
        HDMI1_Final = recv_data['HDMI1_Final']
        HDMI2_FieldRate = recv_data['HDMI2_FieldRate']
        HDMI2_Distinguish = recv_data['HDMI2_Distinguish']
        HDMI2_ConnectState = recv_data['HDMI2_ConnectState']
        HDMI2_HdmiState = recv_data['HDMI2_HdmiState']
        HDMI2_HdcpState = recv_data['HDMI2_HdcpState']
        HDMI2_Final = recv_data['HDMI2_Final']
        SourceImage = recv_data['SourceImage']
        WifiConnection = recv_data['WifiConnection']
        BT_Driver = recv_data['BT_Driver']
        BT_Enable = recv_data['BT_Enable']
        BT_RF = recv_data['BT_RF']
        ScreenTest = recv_data['ScreenTest']
        Saving = recv_data['Saving']
        MIC = recv_data['MIC']
        Vcom = recv_data['Vcom']
        WB = recv_data['WB']

        test_data = Testdata(MachineID, Mac, Widevine, ChinaDrm, Hdcp, ATV_Synchrolock, ATV_FieldRate,
                             ATV_ImageFormat, ATV_SoundFormat, ATV_NoiseIntensity, ATV_Final, DTMB_Synchrolock,
                             DTMB_ImageFormat, DTMB_SignalStrength, DTMB_Final, DVBC_Synchrolock, DVBC_ImageFormat,
                             DVBC_SignalStrength, DVBC_Final, AV_FieldRate, AV_ImageFormat, AV_Final,
                             HDMI1_FieldRate, HDMI1_Distinguish, HDMI1_ConnectState, HDMI1_HdmiState,
                             HDMI1_HdcpState, HDMI1_Final, HDMI2_FieldRate, HDMI2_Distinguish, HDMI2_ConnectState,
                             HDMI2_HdmiState, HDMI2_HdcpState, HDMI2_Final, SourceImage, WifiConnection,
                             BT_Driver, BT_Enable, BT_RF, ScreenTest, Saving, MIC, Vcom, WB)
        db.session.add(test_data)
        db.session.commit()

        recv_ok['return_code'] = '200'
        recv_ok['return_info'] = '数据传输成功'
        return json.dumps(recv_ok, ensure_ascii=False)
    else:
        recv_null['return_code'] = '504'
        recv_null['return_info'] = '请求参数不能为空或者其他原因'
        return json.dumps(recv_null, ensure_ascii=False)


@app.route('/search/', methods=['POST'])
@login_required
def search():
    if request.values.get('MachineID') == '':
        flash('MachineID input is NULL')
        return redirect('/')
    else:
        MachineID = request.values.get('MachineID')
        searchData = Testdata.query.filter_by(MachineID=MachineID).first()
        if searchData == None:
            flash('MachineID not find')
            return redirect('/')
        else:
            return render_template("search.html", searchData=searchData)
