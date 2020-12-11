from tkinter import *
from collections import deque
import tkinter as tk
import matplotlib.pyplot as plt
import timeit
from random import randint
from PIL import ImageTk,Image
from tkinter.ttk import Combobox
import pandas as p
import numpy as np


root = Tk()
root.title("belady algorithm")
root.geometry("750x300")
root.resizable(0, 0)
root.configure(background='light cyan')
#root.configure(background='MistyRose1')
#root.title("OS PROJECT")

title_label = Label(root, text="Page Replacement Algorithm", bg="CYAN", font="comicsansms 30 bold", width=100)
title_label.pack(fill=X)

#mylabel = Label(root,text="Page Replacement Algorithms",font=("Courier",15))
#tlabel.grid(row=1,column=2)

dropdown = [1,2,3,4,5,6,7,8,9,10]


mylabel1 = Label(root, text="Enter the number of frames: ",bg="YELLOW", font="comicsansms 15 bold", width=23)
mylabel1.place(x=40,y=70)

mylabel2 = Label(root, text="Enter the reference string:",bg="YELLOW", font="comicsansms 15 bold", width=21)
mylabel2.place(x=41, y=110)

framevalue = 1
stringvalue = []
stringvalue1 = []

#e=Entry(root, textvariable=framevalue, width=10, font="comicsansms 15 bold")
#e.place(x=350, y=70)

e=Combobox(root, textvariable=framevalue, width=2, value=dropdown, font="comicsansms 15 bold", state="readonly")
e.place(x=350, y=70)

e1=Entry(root, textvariable=stringvalue, width=20, font="comicsansms 15 bold")
e1.place(x=350, y=110)

def FIFO1():
    topw = Toplevel()
    topw.title('First In First Out(FIFO)')
    topw.geometry("900x600")
    topw.configure(background='MistyRose1')
    PageReference=list(map(int, e1.get().strip().split(",")))
    NumberOfFrame=int(e.get())
    print('\n\n#-------------------------------------------------------------------------------------------------------')
    print('# Output of FIFO page replacement algorithm ------------------------------------------------------------')
    print('#-------------------------------------------------------------------------------------------------------')
    print('Number of Frame is: ', NumberOfFrame)
    mylabel = Label(topw, text='Number of Frame is: %d'%(NumberOfFrame), bg="YELLOW", font="comicsansms 15 bold")
    mylabel.place(x=20, y=30)
    print('Page Reference List is: ')
    mylabel1 = Label(topw, text='Page Reference List is:', bg="YELLOW", font="comicsansms 15 bold")
    mylabel1.place(x=20, y=80)
    print(PageReference)
    mylabel2 = Label(topw, text=PageReference, bg="light cyan", font="comicsansms 15 bold")
    mylabel2.place(x=250, y=80)
    print('-------------------------------- Page Frame representation ---------------------------------------------')
    Frame = [np.inf for i in range(NumberOfFrame)]
    print(Frame, '\t # Empty Frame')
    j = 0
    x = 0
    PageFault = 0
    for i in range(len(PageReference)):
        PreIndex = j

        if PageReference[i] not in Frame:
            PageFault += 1
            Frame[j] = PageReference[i]
            j = (j + 1) % NumberOfFrame
        if PreIndex == j:
            print(Frame, '\t No Page Fault (Hit)')
            mylabel3 = Label(topw, text=Frame, bg="orange red", font="comicsansms 15 bold",borderwidth=3,relief=SUNKEN)
            mylabel3.place(x=220, y=140+(40*x))
        else:
            print(Frame, '\t occur Page Fault (Miss)')
            mylabel3 = Label(topw, text=Frame, bg="light cyan", font="comicsansms 15 bold",borderwidth=3,relief=RAISED)
            mylabel3.place(x=220, y=140+(40*x))
        x+=1

    print('--------------------------------------------------------------------------------------------------------')
    print('Number of Page Fault: ', PageFault)
    mylabel3 = Label(topw, text='Page Fault:%d'%(PageFault), font="comicsansms 15 bold")
    mylabel3.place(x=250+(50*NumberOfFrame), y=200 )
    print('--------------------------------------------------------------------------------------------------------')
    topw.mainloop()

def LFU1():
    topw = Toplevel()
    topw.title('Least Recently Used(LRU)')
    topw.geometry("900x600")
    topw.configure(background='MistyRose1')
    PageReference = list(map(int, e1.get().strip().split(",")))
    NumberOfFrame = int(e.get())
    print(
        '\n\n#-------------------------------------------------------------------------------------------------------')
    print('# Output of Least Recently Used algorithm --------------------------------------------------------------')
    print('#-------------------------------------------------------------------------------------------------------')
    print('Number of Frame is: ', NumberOfFrame)
    mylabel = Label(topw, text='Number of Frame is: %d' % (NumberOfFrame), bg="YELLOW", font="comicsansms 15 bold")
    mylabel.place(x=20, y=30)
    print('Page Reference List is: ')
    mylabel1 = Label(topw, text='Page Reference List is:', bg="YELLOW", font="comicsansms 15 bold")
    mylabel1.place(x=20, y=80)
    print(PageReference)
    mylabel2 = Label(topw, text=PageReference, bg="light cyan", font="comicsansms 15 bold")
    mylabel2.place(x=250, y=80)
    print('-------------------------------- Page Frame representation ---------------------------------------------')
    Frame = [np.inf for i in range(NumberOfFrame)]
    IndexList = [i for i in range(NumberOfFrame)]
    print(Frame, '\t # Empty Frame')
    j = 0
    x=0
    PageFault = 0
    for i in range(len(PageReference)):
        if np.inf in Frame:
            index = Frame.index(np.inf)
            Frame[index] = PageReference[i]
            IndexList.pop(0)
            IndexList.append(index)
            PageFault += 1
            print(PageReference[i], Frame, '\t occur Page Fault (Miss)')
            mylabel3 = Label(topw, text=Frame, bg="light cyan", font="comicsansms 15 bold", borderwidth=3, relief=RAISED)
            mylabel3.place(x=220, y=140+(40*x))
        elif PageReference[i] not in Frame:
            Pos = IndexList[0];
            Frame[Pos] = PageReference[i]
            IndexList.pop(0)
            IndexList.append(Pos)
            PageFault += 1
            print(PageReference[i], Frame, '\t occur Page Fault (Miss)')
            mylabel3 = Label(topw, text=Frame, bg="light cyan", font="comicsansms 15 bold", borderwidth=3, relief=RAISED)
            mylabel3.place(x=220, y=140+(40*x))
        else:
            index = Frame.index(PageReference[i])
            index_p = IndexList.index(index)
            IndexList.pop(index_p)
            IndexList.append(index)
            print(PageReference[i], Frame, '\t No Page Fault (Hit)')
            mylabel3 = Label(topw, text=Frame, bg="orange red", font="comicsansms 15 bold", borderwidth=3,relief=SUNKEN)
            mylabel3.place(x=220, y=140+(40*x))
        x+=1

    print('--------------------------------------------------------------------------------------------------------')
    print('Number of Page Fault: ', PageFault)
    mylabel3 = Label(topw, text='Page Fault:%d' % (PageFault), font="comicsansms 15 bold")
    mylabel3.place(x=250 + (50 * NumberOfFrame), y=200)
    print('--------------------------------------------------------------------------------------------------------')
    topw.mainloop()


def OPR1():
    topw = Toplevel()
    topw.title('Optimal Algorithm(OPR)')
    topw.geometry("900x600")
    topw.configure(background='MistyRose1')
    PageReference = list(map(int, e1.get().strip().split(",")))
    NumberOfFrame = int(e.get())

    print(
        '\n\n#-------------------------------------------------------------------------------------------------------')
    print('# Output of Optima Page Replacement algorithm ----------------------------------------------------------')
    print('#-------------------------------------------------------------------------------------------------------')
    print('Number of Frame is: ', NumberOfFrame)
    mylabel = Label(topw, text='Number of Frame is: %d' % (NumberOfFrame), bg="YELLOW", font="comicsansms 15 bold")
    mylabel.place(x=20, y=30)
    print('Page Reference List is: ')
    mylabel2 = Label(topw, text=PageReference, bg="light cyan", font="comicsansms 15 bold")
    mylabel2.place(x=250, y=80)
    print(PageReference)
    mylabel1 = Label(topw, text='Page Reference List is:', bg="YELLOW", font="comicsansms 15 bold")
    mylabel1.place(x=20, y=80)
    print('-------------------------------- Page Frame representation ---------------------------------------------')
    Frame = [np.inf for i in range(NumberOfFrame)]
    print(Frame, '\t # Empty Frame')
    j = 0
    x=0
    PageFault = 0
    for i in range(len(PageReference)):
        if PageReference[i] not in Frame:
            RestList = PageReference[i + 1:len(PageReference)]
            Position = -1
            index = -1
            if np.inf in Frame:
                index = Frame.index(np.inf)
            else:
                for k in range(NumberOfFrame):
                    if Frame[k] in RestList:
                        P = RestList.index(Frame[k])
                        if P > Position:
                            Position = P
                            index = k
                    else:
                        index = k
                        break;
            if index != -1:
                Frame[index] = PageReference[i]
            else:
                Frame[j] = PageReference[i]
                j = (j + 1) % NumberOfFrame
            PageFault += 1
            print(PageReference[i], Frame, '\t occur Page Fault (Miss)')
            mylabel3 = Label(topw, text=Frame, bg="light cyan", font="comicsansms 15 bold", borderwidth=3,relief=RAISED)
            mylabel3.place(x=220, y=140+(40*x))
        else:
            print(PageReference[i], Frame, '\t No Page Fault (Hit)')
            mylabel3 = Label(topw, text=Frame, bg="orange red", font="comicsansms 15 bold", borderwidth=3,relief=SUNKEN)
            mylabel3.place(x=220, y=140+(40*x))
        x+=1

    print('--------------------------------------------------------------------------------------------------------')
    print('Number of Page Fault: ', PageFault)
    mylabel3 = Label(topw, text='Page Fault:%d' % (PageFault), font="comicsansms 15 bold")
    mylabel3.place(x=250 + (50 * NumberOfFrame), y=200)
    print('--------------------------------------------------------------------------------------------------------')

    topw.mainloop()

def LIFO():
    topw = Tk()
    topw.title('Last In First Out(LIFO)')
    topw.geometry("900x600")
    topw.configure(background='MistyRose1')
    PageReference=list(map(int, e1.get().strip().split(",")))
    PageReference.reverse()

    NumberOfFrame=int(e.get())
    print('\n\n#-------------------------------------------------------------------------------------------------------')
    print('# Output of LIFO page replacement algorithm ------------------------------------------------------------')
    print('#-------------------------------------------------------------------------------------------------------')
    print('Number of Frame is: ', NumberOfFrame)
    mylabel = Label(topw, text='Number of Frame is: %d'%(NumberOfFrame), bg="YELLOW", font="comicsansms 15 bold")
    mylabel.place(x=20, y=30)
    print('Page Reference List is: ')
    mylabel1 = Label(topw, text='Page Reference List is:', bg="YELLOW", font="comicsansms 15 bold")
    mylabel1.place(x=20, y=80)
    print(PageReference)
    mylabel2 = Label(topw, text=PageReference, bg="light cyan", font="comicsansms 15 bold")
    mylabel2.place(x=250, y=80)
    print('-------------------------------- Page Frame representation ---------------------------------------------')
    Frame = [np.inf for i in range(NumberOfFrame)]
    print(Frame, '\t # Empty Frame')
    j = 0
    x = 0
    PageFault = 0
    for i in range(len(PageReference)):
        PreIndex = j

        if PageReference[i] not in Frame:
            PageFault += 1
            Frame[j] = PageReference[i]
            j = (j + 1) % NumberOfFrame
        if PreIndex == j:
            print(Frame, '\t No Page Fault (Hit)')
            mylabel3 = Label(topw, text=Frame, bg="orange red", font="comicsansms 15 bold",borderwidth=3,relief=SUNKEN)
            mylabel3.place(x=220, y=140+(40*x))
        else:
            print(Frame, '\t occur Page Fault (Miss)')
            mylabel3 = Label(topw, text=Frame, bg="light cyan", font="comicsansms 15 bold",borderwidth=3,relief=RAISED)
            mylabel3.place(x=220, y=140+(40*x))
        x+=1

    print('--------------------------------------------------------------------------------------------------------')
    print('Number of Page Fault: ', PageFault)
    mylabel3 = Label(topw, text='Page Fault:%d' % (PageFault), font="comicsansms 15 bold")
    mylabel3.place(x=250 + (50 * NumberOfFrame), y=200)
    topw.mainloop()

def LIFO1(capacity):

    PageReference=list(map(int, e1.get().strip().split(",")))
    PageReference.reverse()

    NumberOfFrame=capacity
    print('\n\n#-------------------------------------------------------------------------------------------------------')
    print('# Output of LIFO page replacement algorithm ------------------------------------------------------------')
    print('#-------------------------------------------------------------------------------------------------------')
    print('Number of Frame is: ', NumberOfFrame)

    print('Page Reference List is: ')

    print(PageReference)

    print('-------------------------------- Page Frame representation ---------------------------------------------')
    Frame = [np.inf for i in range(NumberOfFrame)]
    print(Frame, '\t # Empty Frame')
    j = 0
    x = 0

    PageFault = 0
    for i in range(len(PageReference)):
        PreIndex = j

        if PageReference[i] not in Frame:
            PageFault += 1
            Frame[j] = PageReference[i]
            j = (j + 1) % NumberOfFrame
        if PreIndex == j:
            print(Frame, '\t No Page Fault (Hit)')
        else:
            print(Frame, '\t occur Page Fault (Miss)')
        x+=1

    print('--------------------------------------------------------------------------------------------------------')
    print('Number of Page Fault: ', PageFault)

    return PageFault


def LIFOG():
    capacitys = [2,3,4,5,6,7]
    pfs = []

    for capacity in capacitys:
        page_fault = LIFO1(capacity)
        pfs.append(page_fault)

    plt.bar(capacitys, pfs, color='lightblue')
    plt.xticks(capacitys, [str(x) for x in capacitys])
    plt.yticks(pfs, [str(y) for y in pfs])
    plt.xlabel('Capacity')
    plt.ylabel('Page Fault number')

    plt.show()

def rand():
    topw = Tk()
    topw.title('Random(rand)')
    topw.geometry("600x400")
    topw.configure(background='MistyRose1')
    page_array=list(map(int, e1.get().strip().split(",")))
    frames=int(e.get())
    frame_array = []
    frame_index = 0
    page_faults = 0
    hit=0
    insertions = 0
    x=0
    for index, page in enumerate(page_array):
        if page in frame_array:
            print(frame_array)
            mylabel = Label(topw, text=frame_array, bg="orange red", font="comicsansms 15 bold", borderwidth=3,
                             relief=SUNKEN)
            mylabel.place(x=20, y=40 + (40 * x))
            x+=1
            frame_array.insert(toKick, page)
            hit+=1
            continue # should skip to next iteration

        else:
            # Find the victim frame at random
            toKick = randint(0, (frames - 1))

            # Increment the number of page faults
            page_faults = page_faults + 1
            print("page_faults")
            # Put new page into list of frames
            if index < frames:
                frame_array.insert(toKick, page)
                mylabel1 = Label(topw, text=frame_array, bg="light cyan", font="comicsansms 15 bold", borderwidth=3,relief=SUNKEN)
                mylabel1.place(x=20, y=40 + (40 * x))
                x += 1
                print(frame_array)
            else:
                frame_array[toKick] = page
                mylabel2 = Label(topw, text=frame_array, bg="light cyan", font="comicsansms 15 bold", borderwidth=3, relief=SUNKEN)
                mylabel2.place(x=20, y=40 + (40 * x))
                x += 1
                print(frame_array)


    print("RAND: " + str(page_faults))
    print("RAND hit: " + str(hit))
    mylabel4 = Label(topw, text="RAND hit: ", font="comicsansms 15 bold", borderwidth=3, relief=SUNKEN)
    mylabel4.place(x=20, y=40 + (40 * x))
    mylabel3 = Label(topw, text=hit, bg="orange red", font="comicsansms 15 bold", borderwidth=3, relief=SUNKEN)
    mylabel3.place(x=120, y=40 + (40 * x))
    mylabel4 = Label(topw, text="RAND: ", font="comicsansms 15 bold", borderwidth=3, relief=SUNKEN)
    mylabel4.place(x=20, y=80 + (40 * x))
    mylabel3 = Label(topw, text=page_faults, bg="orange red", font="comicsansms 15 bold", borderwidth=3, relief=SUNKEN)
    mylabel3.place(x=120, y=80 + (40 * x))
    print("Total RAND: ",int(page_faults)+int(hit))
    topw.mainloop()

def rand1(frames):
    page_array=list(map(int, e1.get().strip().split(",")))
    frame_array = []
    frame_index = 0
    page_faults = 0
    hit=0
    insertions = 0

    for index, page in enumerate(page_array):
        if page in frame_array:
            print(frame_array)
            hit+=1
            continue # should skip to next iteration

        else:
            # Find the victim frame at random
            toKick = randint(0, (frames - 1))

            # Increment the number of page faults
            page_faults = page_faults + 1
            print("page_faults")
            # Put new page into list of frames
            if index < frames:
                frame_array.insert(toKick, page)
                print(frame_array)
            else:
                frame_array[toKick] = page
                print(frame_array)

    print("RAND: " + str(page_faults))
    print("RAND hit: " + str(hit))
    print("Total RAND: ",int(page_faults)+int(hit))

    return hit

def RANDG():

    capacitys = [2,3,4,5]
    pfs = []

    for capacity in capacitys:
        page_fault = rand1(capacity)
        pfs.append(page_fault)

    plt.bar(capacitys, pfs, color='lightblue')
    plt.xticks(capacitys, [str(x) for x in capacitys])
    plt.yticks(pfs, [str(y) for y in pfs])
    plt.xlabel('Capacity')
    plt.ylabel('Page Fault number')

    plt.show()
# -------------------------------------------------------------------------------------------------------
# User defined function for FIFO -----------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
def FIFO(PageReference, NumberOfFrame):
    Frame = [np.inf for i in range(NumberOfFrame)]
    j = 0
    PageFault = 0
    for i in range(len(PageReference)):
        PreIndex = j
        if PageReference[i] not in Frame:
            PageFault += 1
            Frame[j] = PageReference[i]
            j = (j + 1) % NumberOfFrame
    return PageFault


# -------------------------------------------------------------------------------------------------------
# User defined function for OPR -----------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
def OPR(PageReference, NumberOfFrame):
    Frame = [np.inf for i in range(NumberOfFrame)]
    j = 0
    PageFault = 0
    for i in range(len(PageReference)):
        if PageReference[i] not in Frame:
            RestList = PageReference[i + 1:len(PageReference)]
            Position = -1
            index = -1
            if np.inf in Frame:
                index = Frame.index(np.inf)
            else:
                for k in range(NumberOfFrame):
                    if Frame[k] in RestList:
                        P = RestList.index(Frame[k])
                        if P > Position:
                            Position = P
                            index = k
                    else:
                        index = k
                        break;
            if index != -1:
                Frame[index] = PageReference[i]
            else:
                Frame[j] = PageReference[i]
                j = (j + 1) % NumberOfFrame
            PageFault += 1
    return PageFault


# -------------------------------------------------------------------------------------------------------
# User defined function for Least Recently Used --------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
def LRU(PageReference, NumberOfFrame):
    Frame = [np.inf for i in range(NumberOfFrame)]
    IndexList = [i for i in range(NumberOfFrame)]
    j = 0
    PageFault = 0
    for i in range(len(PageReference)):
        if np.inf in Frame:
            index = Frame.index(np.inf)
            Frame[index] = PageReference[i]
            IndexList.pop(0)
            IndexList.append(index)
            PageFault += 1
        elif PageReference[i] not in Frame:
            Pos = IndexList[0];
            Frame[Pos] = PageReference[i]
            IndexList.pop(0)
            IndexList.append(Pos)
            PageFault += 1
        else:
            index = Frame.index(PageReference[i])
            index_p = IndexList.index(index)
            IndexList.pop(index_p)
            IndexList.append(index)
    return PageFault


# -------------------------------------------------------------------------------------------------------
# User defined function for check the dynamic frame effect  --------------------------------------------------------
# -------------------------------------------------------------------------------------------------------
def DynamicFrame_effect(PageReference, Minimum_Frame, Maximum_Frame):
    PageFault_Array = np.zeros([3, (Maximum_Frame - Minimum_Frame + 1)], dtype=int)
    Frame_Array = np.zeros([(Maximum_Frame - Minimum_Frame + 1)], dtype=int)
    label_array = ['FIFO', 'OPR', 'LRU']
    for NumberOfFrame in (range(Minimum_Frame, (Maximum_Frame + 1))):
        Frame_Array[NumberOfFrame - Minimum_Frame] = NumberOfFrame
        PageFault_Array[0, NumberOfFrame - Minimum_Frame] = FIFO(PageReference, NumberOfFrame)
        PageFault_Array[1, NumberOfFrame - Minimum_Frame] = OPR(PageReference, NumberOfFrame)
        PageFault_Array[2, NumberOfFrame - Minimum_Frame] = LRU(PageReference, NumberOfFrame)
    print('Number of Frame: ', Frame_Array, '\n\nPage fault for each algorithn\n')
    print('Number of Page Reference:', PageReference,'\n')
    for i in range(len(label_array)):
        print(label_array[i], ':', PageFault_Array[i, :])
    for i in range(len(label_array)):
        plt.plot(Frame_Array, PageFault_Array[i, :], marker='o', linewidth=3, label=label_array[i])
    plt.xticks(fontsize=18)
    plt.yticks(fontsize=20)
    plt.title('Frame vs. Page Fault', fontsize=16)
    plt.xlabel('Number of Frames', fontsize=16)
    plt.ylabel('Page Fault', fontsize=16)
    plt.legend()
    plt.show()


# -------------------------------------------------------------------------------------------------------
# Input parapeters -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------

# Pre-defined
def plot():
    Minimum_Frame = 1;
    Maximum_Frame = 10;
    PageReference = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 3]
    #PageReference = [5, 7, 6, 0, 7, 1, 7, 2, 0, 1, 7, 1, 0]
    #PageReference = [0, 2, 1, 6, 4, 0, 1, 0, 3, 1, 2, 1]

    DynamicFrame_effect(PageReference, Minimum_Frame, Maximum_Frame)


def plot2():

    #print("Enter the number of frames: ",end="")
    no_frames = int(e.get())
    #print("Enter the reference string: ",end="")
    page_list = list(map(int, e1.get().strip().split(",")))
    fifolist=fifopra(no_frames,page_list)
    lrulist=lrupra(no_frames,page_list)
    optlist=optpra(no_frames,page_list)
    optimal(fifolist,lrulist,optlist,no_frames)

def plot3():
    # print("Enter the number of frames: ",end="")
    no_frames = int(e.get())
    # print("Enter the reference string: ",end="")
    page_list = list(map(int, e1.get().strip().split(",")))
    fifolist = fifopra(no_frames, page_list)
    lrulist = lrupra(no_frames, page_list)
    optlist = optpra(no_frames, page_list)
    plotdata_fault(fifolist, lrulist, optlist, no_frames)

def plot4():

    # print("Enter the number of frames: ",end="")
    no_frames = int(e.get())
    # print("Enter the reference string: ",end="")
    page_list = list(map(int, e1.get().strip().split(",")))
    fifolist = fifopra(no_frames, page_list)
    lrulist = lrupra(no_frames, page_list)
    optlist = optpra(no_frames, page_list)
    plotdata_time(fifolist, lrulist, optlist, no_frames)


def optimal(fifolist,lrulist,optlist,no_frames):
    topw = Toplevel()
    topw.title('Algorithm Analysis')
    topw.geometry("900x300")
    topw.configure(background='MistyRose1')
    sumfifo={}
    sumlru={}
    sumopt={}
    sumtot=[]
    for i in range(no_frames):
        framestr=i+1
        sf=fifolist[i][0]+fifolist[i][1]
        sl=lrulist[i][0]+lrulist[i][1]
        so=optlist[i][0]+optlist[i][1]
        sumfifo.update({framestr:[fifolist[i][0],fifolist[i][1],sf]})
        sumlru.update({framestr:[lrulist[i][0],lrulist[i][1],sl]})
        sumopt.update({framestr:[optlist[i][0],optlist[i][1],so]})
        if sf<sl and sf<so:
            sumtot.append(["fifo",framestr,fifolist[i][0],fifolist[i][1],sf])
        elif sl<so and sl<sf:
            sumtot.append(["lru",framestr,lrulist[i][0],lrulist[i][1],sl])
        elif so<sl and so<sf:
            sumtot.append(["opt",framestr,optlist[i][0],optlist[i][1],so])
    alg=''
    for i in range(4):
        min=1000
        frame=0
        faultrate=0
        time=0
        if i < 3:
            if i==0:
                for a,b in sumfifo.items():
                    if b[2]<min:
                        min=b[2]
                        frame=a
                        faultrate=b[0]
                        time=b[1]
                print("the best approach for fifo is frame : {} fault rate : {:3.4f} and time : {:.4f}".format(frame,faultrate,time))
                mylabel = Label(topw, text="the best approach for fifo is frame : {} fault rate : {:3.4f} and time : {:.4f}".format(frame,faultrate,time), bg="YELLOW",font="comicsansms 15 bold")
                mylabel.place(x=20, y=30)
            elif i==1:
                for a,b in sumlru.items():
                    if b[2]<min:
                        min=b[2]
                        frame=a
                        faultrate=b[0]
                        time=b[1]
                print("the best approach for lru is frame : {} fault rate : {:3.4f} and time : {:.4f}".format(frame,faultrate,time))
                mylabel = Label(topw,text="the best approach for lru is frame : {} fault rate : {:3.4f} and time : {:.4f}".format(frame,faultrate,time), bg="YELLOW", font="comicsansms 15 bold")
                mylabel.place(x=20, y=80)
            else:
                for a,b in sumopt.items():
                    if b[2]<min:
                        min=b[2]
                        frame=a
                        faultrate=b[0]
                        time=b[1]
                print("the best approach for opt is frame : {} fault rate : {:3.4f} and time : {:.4f}".format(frame,faultrate,time))
                mylabel = Label(topw,text="the best approach for opt is frame : {} fault rate : {:3.4f} and time : {:.4f}".format(frame,faultrate,time), bg="YELLOW", font="comicsansms 15 bold")
                mylabel.place(x=20, y=120)
        if i==3:
            for b in sumtot:
                if b[4]<min:
                    min=b[4]
                    frame=b[1]
                    faultrate=b[2]
                    time=b[3]
                    alg=b[0]
            print("the overall best approach is algorithm : {} frame : {} fault rate : {:3.4f} and time : {:.4f}".format(alg,frame,faultrate,time))
            mylabel = Label(topw,text="the overall best approach is algorithm : {} frame : {} fault rate : {:3.4f} and time : {:.4f}".format(alg,frame,faultrate,time), bg="YELLOW", font="comicsansms 15 bold")
            mylabel.place(x=20, y=170)

    topw.mainloop()

def fifopra(no_frames,page_list):
    retlist=[]
    for t in range(1,no_frames+1):
        start = timeit.default_timer()
        f,fault,top,pf = [],0,0,'No'
        tab_val=[]
        col_label=['String']
        for i in range(t):
            string='frame'+str(i+1)
            col_label.append(string)
        col_label.append('Fault')
        for i in page_list:
            temp=[]
            if i not in f:
                if len(f)<t:
                    f.append(i)
                else:
                    f[top] = i
                    top = (top+1)%t
                fault += 1
                pf = 'Yes'
            else:
                pf = 'No'
            temp.append(i)
            for x in f:
                temp.append(x)
            for x in range(t-len(f)):
                temp.append('-')
            temp.append(pf)
            tab_val.append(temp)
        table=p.DataFrame(columns=col_label,data=tab_val)
        stop = timeit.default_timer()
        if t==no_frames:
            print(table)
            print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(page_list),fault,(fault/len(page_list))*100))
            print('Time: ', stop - start)
        retlist.append((fault/len(page_list),stop - start))
    return retlist



def lrupra(no_frames,page_list):
    retlist=[]
    for t in range(1,no_frames+1):
        start = timeit.default_timer()
        f,st,fault,pf = [],[],0,'No'
        tab_val=[]
        col_label=['String']
        for i in range(t):
            string='frame'+str(i+1)
            col_label.append(string)
        col_label.append('Fault')
        for i in page_list:
            temp=[]
            if i not in f:
                if len(f)<t:
                    f.append(i)
                    st.append(len(f)-1)
                else:
                    ind = st.pop(0)
                    f[ind] = i
                    st.append(ind)
                pf = 'Yes'
                fault += 1
            else:
                st.append(st.pop(st.index(f.index(i))))
                pf = 'No'
            temp.append(i)
            for x in f:
                temp.append(x)
            for x in range(t-len(f)):
                temp.append('-')
            temp.append(pf)
            tab_val.append(temp)
        table=p.DataFrame(columns=col_label,data=tab_val)
        stop = timeit.default_timer()
        if t==no_frames:
            print(table)
            print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(page_list),fault,(fault/len(page_list))*100))
            print('Time: ', stop - start)
        retlist.append((fault/len(page_list),stop - start))
    return retlist



def optpra(no_frames,page_list):
    retlist=[]
    for t in range(1,no_frames+1):
        start = timeit.default_timer()
        f,fault,pf = [],0,'No'
        tab_val=[]
        col_label=['String']
        for i in range(t):
            string='frame'+str(i+1)
            col_label.append(string)
        col_label.append('Fault')
        occurance = [None for i in range(t)]
        for i in range(len(page_list)):
            temp=[]
            if page_list[i] not in f:
                if len(f)<t:
                    f.append(page_list[i])
                else:
                    for x in range(len(f)):
                        if f[x] not in page_list[i+1:]:
                            f[x] = page_list[i]
                            break
                        else:
                            occurance[x] = page_list[i+1:].index(f[x])
                    else:
                        f[occurance.index(max(occurance))] = page_list[i]
                fault += 1
                pf = 'Yes'
            else:
                pf = 'No'
            temp.append(page_list[i])
            for x in f:
                temp.append(x)
            for x in range(t-len(f)):
                temp.append('-')
            temp.append(pf)
            tab_val.append(temp)
        table=p.DataFrame(columns=col_label,data=tab_val)
        stop = timeit.default_timer()
        if t==no_frames:
            print(table)
            print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%"%(len(page_list),fault,(fault/len(page_list))*100))
            print('Time: ', stop - start)
        retlist.append((fault/len(page_list),stop - start))
    return retlist


def plotdata_fault(fifolist,lrulist,optlist,no_frames):
    datarate=[[a[0] for a in fifolist],[b[0] for b in lrulist],[c[0] for c in optlist]]
    #datatime=[[a[1] for a in fifolist],[b[1] for b in lrulist],[c[1] for c in optlist]]

    fig, ax= plt.subplots()

    width=0.33
    color_list = ['b', 'g', 'r']
    X=np.arange(no_frames)
    Xticks=[a+0.25 for a in X]
    Xtickslabels=[i+1 for i in range(no_frames)]


    ax.bar(X+0.00,datarate[0],width = 0.25,color = '#bada55',label='first in first out')
    ax.bar(X+0.25,datarate[1],width = 0.25,color = '#7fe5f0',label='least recently used')
    ax.bar(X+0.50,datarate[2],width = 0.25,color = '#f7347a',label='optimal')

    ax.set_ylabel('Fault rate')
    ax.set_xlabel('number of frames')
    ax.set_title('Fault rate in each algorithm')
    ax.set_xticks(Xticks)
    ax.set_xticklabels(Xtickslabels)
    ax.legend()

    plt.show()

def plotdata_time(fifolist,lrulist,optlist,no_frames):
    #datarate=[[a[0] for a in fifolist],[b[0] for b in lrulist],[c[0] for c in optlist]]
    datatime=[[a[1] for a in fifolist],[b[1] for b in lrulist],[c[1] for c in optlist]]

    fig, ax= plt.subplots()

    width=0.33
    color_list = ['b', 'g', 'r']
    X=np.arange(no_frames)
    Xticks=[a+0.25 for a in X]
    Xtickslabels=[i+1 for i in range(no_frames)]


    ax.bar(X+0.00,datatime[0],width = 0.25,color = '#bada55',label='first in first out')
    ax.bar(X+0.25,datatime[1],width = 0.25,color = '#7fe5f0',label='least recently used')
    ax.bar(X+0.50,datatime[2],width = 0.25,color = '#f7347a',label='optimal')

    ax.set_ylabel('Execution time')
    ax.set_xlabel('number of frames')
    ax.set_title('Execution time in each algorithm')
    ax.set_xticks(Xticks)
    ax.set_xticklabels(Xtickslabels)
    ax.legend()

    plt.show()

def algo():
    top=Toplevel()
    top.geometry("721x480")
    canvas=Canvas(top,width=1153,height=768,background='light cyan')
    top.title('Algorithm')
    #my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Jaydip\\Downloads\\WhatsApp Image 2020-12-08 at 11.59.03 AM.jpeg"))

    canvas.create_image(0,0,anchor=NW)
    canvas.pack()

    myButton1 = Button(top, text="FIFO", bg="ORANGE2", width=10, height=1, command=FIFO1, font="comicsansms",
                       borderwidth=5)
    myButton1.place(x=100, y=100)

    myButton2 = Button(top, text="LRU", bg="ORANGE2", width=10, height=1, command=LFU1, font="comicsansms",
                       borderwidth=5)
    myButton2.place(x=300, y=100)

    myButton3 = Button(top, text="OPR", bg="ORANGE2", width=10, height=1, command=OPR1, font="comicsansms",
                       borderwidth=5)
    myButton3.place(x=500, y=100)

    myButton4 = Button(top, text="GRAPH(Analyze)", bg="ORANGE2", width=15, height=1, command=plot, font="comicsansms",
                       borderwidth=5)
    myButton4.place(x=300, y=350)

    Button(top, text='EXIT', width=10, height=1, bg='grey', fg='white', font="comicsansms", command=root.destroy,
           borderwidth=5).place(x=310, y=400)

    myButton5 = Button(top, text="BEST ALGORITHM", bg="ORANGE2", width=15, height=1, command=plot2, font="comicsansms",
                       borderwidth=5)
    myButton5.place(x=100, y=300)

    myButton6 = Button(top, text="GRAPH(Faults)", bg="ORANGE2", width=12, height=1, command=plot3, font="comicsansms",
                       borderwidth=5)
    myButton6.place(x=300, y=300)

    myButton7 = Button(top, text="GRAPH(time)", bg="ORANGE2", width=15, height=1, command=plot4, font="comicsansms",
                       borderwidth=5)
    myButton7.place(x=500, y=300)

    top.mainloop()

def adva():
    top = Toplevel()
    top.geometry("721x380")
    canvas = Canvas(top, width=1153, height=768,background='light cyan')
    top.title('Algorithm')
    #my_img = ImageTk.PhotoImage(Image.open("C:\\Users\\Jaydip\\Downloads\\WhatsApp Image 2020-12-08 at 11.59.03 AM.jpeg"))

    canvas.create_image(0, 0, anchor=NW)
    canvas.pack()

    myButton1 = Button(top, text="RANDOM",bg="ORANGE2", width=10, height=1, command=rand, font="comicsansms",borderwidth=5)
    myButton1.place(x=200, y=100)

    myButton2 = Button(top, text="LIFO",bg="ORANGE2", width=10, height=1, command=LIFO, font="comicsansms",borderwidth=5)
    myButton2.place(x=400, y=100)

    myButton3 = Button(top, text="LIFO(graph)",bg="ORANGE2", width=10, height=1, command=LIFOG, font="comicsansms",borderwidth=5)
    myButton3.place(x=400, y=200)

    myButton4 = Button(top, text="RAND(graph)", bg="ORANGE2", width=15, height=1, command=RANDG, font="comicsansms",
                       borderwidth=5)
    myButton4.place(x=200, y=200)

    Button(top, text='EXIT', width=10, height=1, bg='grey', fg='white', font="comicsansms", command=root.destroy,
           borderwidth=5).place(x=310, y=300)

    top.mainloop()

myButton = Button(root, text="GENERAL ALGO",bg="ORANGE2", width=20, height=1, command=algo, font="comicsansms",borderwidth=5)
myButton.place( x=150, y=200 )

myButton = Button(root, text="OTHER ALGO",bg="ORANGE2", width=20, height=1, command=adva, font="comicsansms",borderwidth=5)
myButton.place( x=400, y=200 )

Button(root, text='EXIT', width=10, height=1, bg='grey', fg='white', font="comicsansms", command=root.destroy,
           borderwidth=5).place(x=310, y=250)

root.mainloop()
