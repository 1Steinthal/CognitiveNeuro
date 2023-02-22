#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on februar 12, 2023, at 16:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard


from triggers import setParallelData #My own script


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'EEG'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='"C:\\Users\\45239\\Documents\\PythonScripts\\230208-EEGExp\\EEG_THrev.py"',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1280, 720], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()


##INITIALIZING COMPONENTS
trialCClock = core.Clock() #Overvej om vi også behøver trialDbClock, osv
C4 = sound.Sound('261.63', secs=1.0, stereo=True, hamming=True,
    name='C4')
C4.setSound('261.63', secs=1.0, hamming=True)
C4.setVolume(1.0, log = False)

Db = sound.Sound('277.18', secs=1.0, stereo=True, hamming=True,
    name='Db')
Db.setSound('277.18', secs=1.0, hamming=True)
Db.setVolume(1.0, log = False)

D = sound.Sound('293.66', secs=1.0, stereo=True, hamming=True,
    name='D')
D.setSound('293.66', secs=1.0, hamming=True)
D.setVolume(1.0, log = False)

Eb = sound.Sound('311.13', secs=1.0, stereo=True, hamming=True,
    name='Eb')
Eb.setSound('311.13', secs=1.0, hamming=True)
Eb.setVolume(1.0, log = False)

E = sound.Sound('329.63', secs=1.0, stereo=True, hamming=True,
    name='E')
E.setSound('329.63', secs=1.0, hamming=True)
E.setVolume(1.0, log = False)

F = sound.Sound('349.23', secs=1.0, stereo=True, hamming=True,
    name='F')
F.setSound('349.23', secs=1.0, hamming=True)
F.setVolume(1.0, log = False)

Gb = sound.Sound('369.99', secs=1.0, stereo=True, hamming=True,
    name='Gb')
Gb.setSound('369.99', secs=1.0, hamming=True)
Gb.setVolume(1.0, log = False)

G = sound.Sound('392', secs=1.0, stereo=True, hamming=True,
    name='G')
G.setSound('392', secs=1.0, hamming=True)
G.setVolume(1.0, log = False)

Ab = sound.Sound('415.30', secs=1.0, stereo=True, hamming=True,
    name='Ab')
Ab.setSound('415.30', secs=1.0, hamming=True)
Ab.setVolume(1.0, log = False)

A = sound.Sound('440', secs=1.0, stereo=True, hamming=True,
    name='A')
A.setSound('440', secs=1.0, hamming=True)
A.setVolume(1.0, log = False)

Bb = sound.Sound('466.16', secs=1.0, stereo=True, hamming=True,
    name='Bb')
Bb.setSound('466.16', secs=1.0, hamming=True)
Bb.setVolume(1.0, log = False)

B = sound.Sound('493.88', secs=1.0, stereo=True, hamming=True,
    name='B')
B.setSound('493.88', secs=1.0, hamming=True)
B.setVolume(1.0, log = False)

C5 = sound.Sound('523.25', secs=1.0, stereo=True, hamming=True,
    name='C5')
C5.setSound('523.25', secs=1.0, hamming=True)
C5.setVolume(1.0, log = False)

#C er uden indexering, Db er med b, Eb er med c, Gb er med d, Ab er med e og Bb er med f


# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine



def func_trialC(note):
    # ------Prepare to start Routine "trialC"-------
    continueRoutine = True
    routineTimer.add(15.500000)

    # keep track of which components have finished
    if note == 'C':
        trialCComponents = [C4, D, E, F, G, A, B, C5]
    if note == 'Db':
        trialCComponents = [C4, Db, E, F, G, A, B, C5]
    if note == 'Eb':
        trialCComponents = [C4, D, Eb, F, G, A, B, C5]
    if note == 'Gb':
        trialCComponents = [C4, Db, E, F, Gb, A, B, C5]
    if note == 'Ab':
        trialCComponents = [C4, D, E, F, G, Ab, B, C5]
    if note == 'Bb':
        trialCComponents = [C4, Db, E, F, G, A, Bb, C5]


    for thisComponent in trialCComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialCClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    pullTriggerDown = False

    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialCClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialCClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # start/stop C4
        if C4.status == NOT_STARTED and tThisFlip >= 4 - frameTolerance:
            # keep track of start time/frame for later
            C4.frameNStart = frameN  # exact frame index
            C4.tStart = t  # local t and not account for scr refresh
            C4.tStartRefresh = tThisFlipGlobal  # on global time
            win.callOnFlip(setParallelData, trial['congruent']) #Prepare trigger
            pullTriggerDown = True #Pull trigger
            C4.play(when=win)  # sync with win flip
        
        if C4.status == STARTED:
            #Pulling trigger again
            if pullTriggerDown:
                win.callOnFlip(setParallelData, 0)
                pullTriggerDown = False

            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C4.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                C4.tStop = t  # not accounting for scr refresh
                C4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C4, 'tStopRefresh')  # time at next scr refresh
                C4.stop()

        if note == 'Db':
            #Start Db
            if Db.status == NOT_STARTED and tThisFlip >= 5.5 - frameTolerance:
                # keep track of start time/frame for later
                Db.frameNStart = frameN  # exact frame index
                Db.tStart = t  # local t and not account for scr refresh
                Db.tStartRefresh = tThisFlipGlobal  # on global time
                win.callOnFlip(setParallelData, trial['incongruentDb']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                Db.play(when=win)  # sync with win flip

            if Db.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Db.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    Db.tStop = t  # not accounting for scr refresh
                    Db.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Db, 'tStopRefresh')  # time at next scr refresh
                    Db.stop()
        else:
            # start/stop D
            if D.status == NOT_STARTED and tThisFlip >= 5.5 - frameTolerance:
                # keep track of start time/frame for later
                D.frameNStart = frameN  # exact frame index
                D.tStart = t  # local t and not account for scr refresh
                D.tStartRefresh = tThisFlipGlobal  # on global time
                win.callOnFlip(setParallelData, trial['congruent']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                D.play(when=win)  # sync with win flip

            if D.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > D.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    D.tStop = t  # not accounting for scr refresh
                    D.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(D, 'tStopRefresh')  # time at next scr refresh
                    D.stop()


        if note == 'Eb':
            # start/stop Eb
            if Eb.status == NOT_STARTED and tThisFlip >= 7 - frameTolerance:
                # keep track of start time/frame for later
                Eb.frameNStart = frameN  # exact frame index
                Eb.tStart = t  # local t and not account for scr refresh
                Eb.tStartRefresh = tThisFlipGlobal  # on global time
                win.callOnFlip(setParallelData, trial['incongruentEb']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                Eb.play(when=win)  # sync with win flip

            if Eb.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Eb.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    Eb.tStop = t  # not accounting for scr refresh
                    Eb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Eb, 'tStopRefresh')  # time at next scr refresh
                    Eb.stop()

        else:
            # start/stop E
            if E.status == NOT_STARTED and tThisFlip >= 7 - frameTolerance:
                # keep track of start time/frame for later
                E.frameNStart = frameN  # exact frame index
                E.tStart = t  # local t and not account for scr refresh
                E.tStartRefresh = tThisFlipGlobal  # on global time
                if note == 'Db':
                    win.callOnFlip(setParallelData, trial['postincongruent']) #Prepare trigger
                else:
                    win.callOnFlip(setParallelData, trial['congruent']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                E.play(when=win)  # sync with win flip

            if E.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > E.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    E.tStop = t  # not accounting for scr refresh
                    E.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(E, 'tStopRefresh')  # time at next scr refresh
                    E.stop()

        # start/stop F
        if F.status == NOT_STARTED and tThisFlip >= 8.5 - frameTolerance:
            # keep track of start time/frame for later
            F.frameNStart = frameN  # exact frame index
            F.tStart = t  # local t and not account for scr refresh
            F.tStartRefresh = tThisFlipGlobal  # on global time
            if note == 'Eb':
                win.callOnFlip(setParallelData, trial['postincongruent']) #Prepare trigger
            else:
                win.callOnFlip(setParallelData, trial['congruent']) #Prepare trigger
            pullTriggerDown = True #Pull trigger
            F.play(when=win)  # sync with win flip

        if F.status == STARTED:
            # Pulling trigger again
            if pullTriggerDown:
                win.callOnFlip(setParallelData, 0)
                pullTriggerDown = False
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > F.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                F.tStop = t  # not accounting for scr refresh
                F.frameNStop = frameN  # exact frame index
                win.timeOnFlip(F, 'tStopRefresh')  # time at next scr refresh
                F.stop()


        if note == 'Gb':
            # start/stop G
            if Gb.status == NOT_STARTED and tThisFlip >= 10 - frameTolerance:
                # keep track of start time/frame for later
                Gb.frameNStart = frameN  # exact frame index
                Gb.tStart = t  # local t and not account for scr refresh
                Gb.tStartRefresh = tThisFlipGlobal  # on global time
                win.callOnFlip(setParallelData, trial['incongruentGb']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                Gb.play(when=win)  # sync with win flip

            if Gb.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Gb.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    Gb.tStop = t  # not accounting for scr refresh
                    Gb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Gb, 'tStopRefresh')  # time at next scr refresh
                    Gb.stop()

        else:
            # start/stop G
            if G.status == NOT_STARTED and tThisFlip >= 10 - frameTolerance:
                # keep track of start time/frame for later
                G.frameNStart = frameN  # exact frame index
                G.tStart = t  # local t and not account for scr refresh
                G.tStartRefresh = tThisFlipGlobal  # on global time
                win.callOnFlip(setParallelData, trial['congruent']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                G.play(when=win)  # sync with win flip

            if G.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > G.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    G.tStop = t  # not accounting for scr refresh
                    G.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(G, 'tStopRefresh')  # time at next scr refresh
                    G.stop()



        if note == 'Ab':
            # start/stop A
            if Ab.status == NOT_STARTED and tThisFlip >= 11.5 - frameTolerance:
                # keep track of start time/frame for later
                Ab.frameNStart = frameN  # exact frame index
                Ab.tStart = t  # local t and not account for scr refresh
                Ab.tStartRefresh = tThisFlipGlobal  # on global time
                win.callOnFlip(setParallelData, trial['incongruentAb']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                Ab.play(when=win)  # sync with win flip

            if Ab.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Ab.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    Ab.tStop = t  # not accounting for scr refresh
                    Ab.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Ab, 'tStopRefresh')  # time at next scr refresh
                    Ab.stop()


        else:
            # start/stop A
            if A.status == NOT_STARTED and tThisFlip >= 11.5 - frameTolerance:
                # keep track of start time/frame for later
                A.frameNStart = frameN  # exact frame index
                A.tStart = t  # local t and not account for scr refresh
                A.tStartRefresh = tThisFlipGlobal  # on global time
                if note == 'Gb':
                    win.callOnFlip(setParallelData, trial['postincongruent']) #Prepare trigger
                else:
                    win.callOnFlip(setParallelData, trial['congruent']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                A.play(when=win)  # sync with win flip

            if A.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > A.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    A.tStop = t  # not accounting for scr refresh
                    A.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(A, 'tStopRefresh')  # time at next scr refresh
                    A.stop()



        if note == 'Bb':
            # start/stop B
            if Bb.status == NOT_STARTED and tThisFlip >= 13 - frameTolerance:
                # keep track of start time/frame for later
                Bb.frameNStart = frameN  # exact frame index
                Bb.tStart = t  # local t and not account for scr refresh
                Bb.tStartRefresh = tThisFlipGlobal  # on global time
                win.callOnFlip(setParallelData, trial['incongruentBb']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                Bb.play(when=win)  # sync with win flip

            if Bb.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Bb.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    Bb.tStop = t  # not accounting for scr refresh
                    Bb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Bb, 'tStopRefresh')  # time at next scr refresh
                    Bb.stop()


        else:
            # start/stop B
            if B.status == NOT_STARTED and tThisFlip >= 13 - frameTolerance:
                # keep track of start time/frame for later
                B.frameNStart = frameN  # exact frame index
                B.tStart = t  # local t and not account for scr refresh
                B.tStartRefresh = tThisFlipGlobal  # on global time
                if note == 'Ab':
                    win.callOnFlip(setParallelData, trial['postincongruent']) #Prepare trigger
                else:
                    win.callOnFlip(setParallelData, trial['congruent']) #Prepare trigger
                pullTriggerDown = True  # Pull trigger
                B.play(when=win)  # sync with win flip

            if B.status == STARTED:
                # Pulling trigger again
                if pullTriggerDown:
                    win.callOnFlip(setParallelData, 0)
                    pullTriggerDown = False
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > B.tStartRefresh + 1.0 - frameTolerance:
                    # keep track of stop time/frame for later
                    B.tStop = t  # not accounting for scr refresh
                    B.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(B, 'tStopRefresh')  # time at next scr refresh
                    B.stop()

        # start/stop C5
        if C5.status == NOT_STARTED and tThisFlip >= 14.5 - frameTolerance:
            # keep track of start time/frame for later
            C5.frameNStart = frameN  # exact frame index
            C5.tStart = t  # local t and not account for scr refresh
            C5.tStartRefresh = tThisFlipGlobal  # on global time
            if note == 'Bb':
                win.callOnFlip(setParallelData, trial['postincongruent']) #Prepare trigger
            else:
                win.callOnFlip(setParallelData, trial['congruent']) #Prepare trigger
            pullTriggerDown = True #Pull trigger
            C5.play(when=win)  # sync with win flip
            
        if C5.status == STARTED:
            #Pulling trigger again
            if pullTriggerDown:
                win.callOnFlip(setParallelData, 0)
                pullTriggerDown = False
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > C5.tStartRefresh + 1.0 - frameTolerance:
                # keep track of stop time/frame for later
                C5.tStop = t  # not accounting for scr refresh
                C5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(C5, 'tStopRefresh')  # time at next scr refresh
                C5.stop()

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialCComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trialC"-------
    for thisComponent in trialCComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    C4.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('C4.started', C4.tStartRefresh)
    thisExp.addData('C4.stopped', C4.tStopRefresh)

    if note == 'Db':
        Db.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('Db.started', Db.tStartRefresh)
        thisExp.addData('Db.stopped', Db.tStopRefresh)
    else:
        D.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('D.started', D.tStartRefresh)
        thisExp.addData('D.stopped', D.tStopRefresh)

    if note == 'Eb':
        Eb.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('Eb.started', Eb.tStartRefresh)
        thisExp.addData('Eb.stopped', Eb.tStopRefresh)
    else:
        E.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('E.started', E.tStartRefresh)
        thisExp.addData('E.stopped', E.tStopRefresh)

    F.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('F.started', F.tStartRefresh)
    thisExp.addData('F.stopped', F.tStopRefresh)

    if note == 'Gb':
        Gb.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('Gb.started', Gb.tStartRefresh)
        thisExp.addData('Gb.stopped', Gb.tStopRefresh)
    else:
        G.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('G.started', G.tStartRefresh)
        thisExp.addData('G.stopped', G.tStopRefresh)

    if note == 'Ab':
        Ab.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('Ab.started', Ab.tStartRefresh)
        thisExp.addData('Ab.stopped', Ab.tStopRefresh)
    else:
        A.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('A.started', A.tStartRefresh)
        thisExp.addData('A.stopped', A.tStopRefresh)


    if note == 'Bb':
        Bb.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('Bb.started', Bb.tStartRefresh)
        thisExp.addData('Bb.stopped', Bb.tStopRefresh)
    else:
        B.stop()  # ensure sound has stopped at end of routine
        thisExp.addData('B.started', B.tStartRefresh)
        thisExp.addData('B.stopped', B.tStopRefresh)


    C5.stop()  # ensure sound has stopped at end of routine
    thisExp.addData('C5.started', C5.tStartRefresh)
    thisExp.addData('C5.stopped', C5.tStopRefresh)




##PLAYING THE ACTUAL SCRIPT

seq = ['C','C','Eb','Bb','Db','Gb','C','C','C','Db','Gb','C','Bb','Bb','C','Db','C','C','Gb','Bb','Eb','C','Bb','C','C','C','Db','C','Gb','Eb','C','C','Ab','C','Gb','Db','C','C','C','Ab','C','Bb','C','C']
for trial in seq:
    func_trialC(trial)




# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
