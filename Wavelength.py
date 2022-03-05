#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


st.title('Written by Omid Ghamiloo')


# In[2]:


h = 6.626 * (10**-34) #J
c = 299792458 #m/sec


# In[3]:


def Un_micro(x,unit):
    U = ['m','cm','nm']
    L = [1000000,10000,0.001]
    for i,j in zip(U,L):
        if unit == i:
            result = x * j 
    return result


# In[4]:


L = st.sidebar.text_input('Lambda','0.4')
LUnits = ['Micro_m','m','cm','nm']
Lambda_units = st.sidebar.selectbox('Lambda_Unit',LUnits)
if Lambda_units != 'Micro_m':
    L_Mm = Un_micro(float(L),Lambda_units)
else:
    L_Mm = float(L)
L_nm = L_Mm * 1000
L_cm = L_Mm * 1e-4
L_m = L_cm * 0.01
f_MHz = c/L_Mm
f_Hz = f_MHz * 1E+6
f_GHz = f_MHz * 1E-3
f_THz = f_GHz * 0.001
E_Mj = f_MHz * h
E_j = E_Mj * 1000000
E_ev = E_j * 6241506000000000000
E_mev = E_ev * 1e-6
st.sidebar.title('Wavelength')
st.sidebar.text(str("%.4g" %L_Mm)+' Mm')
st.sidebar.text(str("%.4g" %L_nm)+' nm')
st.sidebar.text(str("%.4g" %L_cm)+' cm')
st.sidebar.text(str("%.4g" %L_m)+' m')
st.sidebar.title('Freqency')
st.sidebar.text(str("%.4g" %f_Hz)+' Hz')
st.sidebar.text(str("%.4g" %f_MHz)+' MHz')
st.sidebar.text(str("%.4g" %f_GHz)+' GHz')
st.sidebar.title('Energy')
st.sidebar.text(str("%.4g" %E_j)+' j')
st.sidebar.text(str("%.4g" %E_Mj)+' Mj')
st.sidebar.text(str("%.4g" %E_ev)+' eV')


# In[185]:


def IR_w(w):
    #Wavelength Micro m
    fig1 = plt.figure(figsize = (15,2))
    plt.plot()
    plt.xlim(0.15,20)
    plt.ylim(-1,1)
    plt.axvline(0.75, -2, 2, c='black', ls='solid', lw = 2)
    plt.axvline(1.4, -2, 2, c='black', ls='--', lw = 2)
    plt.axvline(3, -2, 2, c='black', ls='--', lw = 2)
    plt.axvline(8, -2, 2, c='black', ls='--', lw = 2)
    plt.axvline(15, -2, 2, c='black', ls='--', lw = 2)
    if w>20:
        w=19
    plt.axvline(w, -2, 1, c='brown', ls=':',lw = 3)
    plt.text(0.35, 0.5, 'V', color='black', fontdict={'fontsize': 15})
    plt.text(0.74, 0.5, 'NIR', color='black', fontdict={'fontsize': 15})
    plt.text(1.9, 0.5, 'SWIR', color='black', fontdict={'fontsize': 15})
    plt.text(5, 0.5, 'MWIR', color='black', fontdict={'fontsize': 20})
    plt.text(11, 0.5, 'LWIR', color='black', fontdict={'fontsize': 20})
    plt.text(17, 0.5, 'FIR', color='black', fontdict={'fontsize': 20})
    plt.title('IR Wavelength',size=20)
    plt.xlabel('Micrometer',size=14)
    plt.yticks([])
    st.pyplot(fig1)
    
def IR_f(f):
    #Frequency THz
    fig1 = plt.figure(figsize = (15,2))
    plt.plot()
    plt.xlim(450,10)
    plt.ylim(-1,1)
    plt.axvline(400, -2, 2, c='black', ls='solid',lw = 2)
    plt.axvline(214, -2, 2, c='black', ls='--',lw = 2)
    plt.axvline(100, -2, 2, c='black', ls='--',lw = 2)
    plt.axvline(37, -2, 2, c='black', ls='--',lw = 2)
    plt.axvline(20, -2, 2, c='black', ls='--',lw = 2)
    if f<= 10:
        f = 11
    plt.axvline(f, -2, 1, c='brown', ls=':',lw = 3)
    plt.text(440, 0.5, 'Visible', color='black', fontdict={'fontsize': 20})
    plt.text(330, 0.5, 'NIR', color='black', fontdict={'fontsize': 20})
    plt.text(170, 0.5, 'SWIR', color='black', fontdict={'fontsize': 20})
    plt.text(85, 0.5, 'MWIR', color='black', fontdict={'fontsize': 20})
    plt.text(35, 0.5, 'LWIR', color='black', fontdict={'fontsize': 10})
    plt.text(18, 0.5, 'FIR', color='black', fontdict={'fontsize': 10})
    plt.title('IR Frequency',size=20)
    plt.xlabel('THz',size=14)
    plt.yticks([])
    st.pyplot(fig1)
    
def IR_e(e):
    #Energy meV
    fig1 = plt.figure(figsize = (15,2))
    plt.plot()
    plt.xlim(1900,1)
    plt.ylim(-1,1)
    plt.axvline(83, -1, 1, c='black', ls='--',lw = 2)
    plt.axvline(155, -1, 1, c='black', ls='--',lw = 2)
    plt.axvline(413, -1, 1, c='black', ls='--',lw = 2)
    plt.axvline(886, -1, 1, c='black', ls='--',lw = 2)
    plt.axvline(1653, -2, 2, c='black', ls='solid',lw = 2)
    plt.axvline(e, -2, 1, c='brown', ls=':',lw = 3)
    plt.text(1850, 0.5, 'Visible', color='black', fontdict={'fontsize': 20})
    plt.text(1300, 0.5, 'NIR', color='black', fontdict={'fontsize': 20})
    plt.text(700, 0.5, 'SWIR', color='black', fontdict={'fontsize': 20})
    plt.text(350, 0.5, 'MWIR', color='black', fontdict={'fontsize': 20})
    plt.text(140, 0.5, 'LWIR', color='black', fontdict={'fontsize': 10})
    plt.text(45, 0.5, 'FIR', color='black', fontdict={'fontsize': 10})
    plt.title('IR Energy',size=20)
    plt.xlabel('meV',size=14)
    plt.yticks([])
    st.pyplot(fig1)


# In[194]:


def visible_w(w):
    #Wavelength nm
    fig1 = plt.figure(figsize = (15,2))
    plt.plot()
    plt.xlim(250,950)
    plt.ylim(-1,1)
    plt.axvline(750, -2, 2, c='black', ls='solid',lw = 2)
    plt.axvline(400, -2, 2, c='black', ls='solid',lw = 2)
    plt.axvline(w, -2, 1, c='brown', ls=':',lw = 3)
    plt.text(310, 0.5, 'UV', color='black', fontdict={'fontsize': 20})
    plt.text(530, 0.5, 'Visible', color='black', fontdict={'fontsize': 20})
    plt.text(860, 0.5, 'IR', color='black', fontdict={'fontsize': 20})
    rainbow_rgb = {(400, 440): '#8b00ff', (440, 460): '#4b0082',
                (460, 500): '#0000ff', (500, 570): '#00ff00',
                (570, 590): '#ffff00', (590, 620): '#ff7f00',
                (620, 750): '#ff0000'}
    for i,j in zip(rainbow_rgb.keys(),rainbow_rgb.values()):
        plt.axvspan(i[0],i[1],color=j)
    plt.title('Wavelength',size=20)
    plt.xlabel('Nanometer',size=14)
    plt.yticks([])
    st.pyplot(fig1)
    
def visible_f(f):
    #Frequency THz
    fig1 = plt.figure(figsize = (15,2))
    plt.plot()
    plt.xlim(900,200)
    plt.ylim(-1,1)
    plt.axvline(400, -2, 2, c='black', ls='solid',lw = 2)
    plt.axvline(750, -2, 2, c='black', ls='solid',lw = 2)
    plt.axvline(f, -2, 1, c='brown', ls=':',lw = 3)
    rainbow_rgb = {(750, 710): '#8b00ff', (710, 690): '#4b0082',
                (690, 650): '#0000ff', (650, 580): '#00ff00',
                (580, 560): '#ffff00', (560, 530): '#ff7f00',
                (530, 400): '#ff0000'}
    for i,j in zip(rainbow_rgb.keys(),rainbow_rgb.values()):
        plt.axvspan(i[0],i[1],color=j)
    plt.text(840, 0.5, 'UV', color='black', fontdict={'fontsize': 20})
    plt.text(620, 0.5, 'Visible', color='black', fontdict={'fontsize': 20})
    plt.text(290, 0.5, 'IR', color='black', fontdict={'fontsize': 20})
    plt.title('Frequency',size=20)
    plt.xlabel('THz',size=14)
    plt.yticks([])
    st.pyplot(fig1)
    
def visible_e(e):
    #Energy eV
    fig1 = plt.figure(figsize = (15,2))
    plt.plot()
    plt.xlim(3.9,0.8)
    plt.ylim(-1,1)
    plt.axvline(3.26, -1, 1, c='black', ls='solid',lw = 2)
    plt.axvline(1.65, -2, 2, c='black', ls='solid',lw = 2)
    plt.axvline(e, -2, 1, c='brown', ls=':',lw = 3)
    rainbow_rgb = {(2.75, 3.26): '#8b00ff', (2.56, 2.75): '#4b0082',
                (2.48, 2.56): '#0000ff', (2.19, 2.48): '#00ff00',
                (2.10, 2.19): '#ffff00', (1.98, 2.10): '#ff7f00',
                (1.65, 1.98): '#ff0000'}
    for i,j in zip(rainbow_rgb.keys(),rainbow_rgb.values()):
        plt.axvspan(i[0],i[1],color=j)
    plt.text(3.7, 0.5, 'UV', color='black', fontdict={'fontsize': 20})
    plt.text(2.5, 0.5, 'Visible', color='black', fontdict={'fontsize': 20})
    plt.text(1.2, 0.5, 'IR', color='black', fontdict={'fontsize': 20})
    plt.title('Energy',size=20)
    plt.xlabel('eV',size=14)
    plt.yticks([])
    st.pyplot(fig1)


# In[195]:


if ((L_nm >= 400) & (L_nm <= 750)):
    visible_w(L_nm)
    visible_f(f_THz)
    visible_e(E_ev)
elif ((L_Mm >= 0.75) & (L_Mm <= 1000)):
    IR_w(L_Mm)
    IR_f(f_THz)
    IR_e(E_mev)

