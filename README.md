IMPLEMENTING FACE DETECTION USING OPEN CV IN A VIDEO FILE OR LIVESTREAM


In this program I have aimed to create a simple yeat useful program for face detection with opencv . The program uses Haarcascade frontal face detector . 
Which is a pre-trained face detection algorithm present in opencv library . I have also used principle of creating masks which helps to mark the 
face in the detected video and also the concept of looping through frames so as to display the video . Also the error handling is done using
the try except block which launches a messagewindow (saying the video file has ended )which helps to manage the error 'end of frames'
which usually happens when video file durations is run out . By developing this project i was able to understand clearly about the opencv librabry
and the importance of computer visisonn . 

STEPS TO RUN THE FILE :
INPUT THE PATH(RELATIVE/ABSOLUTE)in the input line if you want to pass an existing video file ,if you want to use webcam livestream input0
RUN THE CODE AND IT WILL ENCLOSE IN A BLUE RECTANGULAR BOX THE DETECTED FACES IN THE VIDEO FILE/LIVESTREAM
WHEN THE VIDEO FILE ENDS A DIALOGUE BOX POPS UP SHOWING END OF VIDEO FILE WHICH HELPS TO HANDLE THE OPEN CV ERROR .
