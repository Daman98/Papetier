from django.shortcuts import render, redirect
from .models import question
from .forms import questionForm_text,questionForm_image,inputForm
from django.http import HttpResponse, JsonResponse
import random
# Create your views here.
def que_list(request):
    return render(request, 'app1/post_list.html', {})

def main(request):
    return render(request, 'app1/main.html', {})

def post_new_text(request):
    if request.method =="POST":
        question_form= questionForm_text(request.POST,request.FILES)
        if question_form.is_valid():
            question_form=question_form.save(commit=False)
            question_form.save()
            
            return redirect('/post/new/bytext/')
    else :
        question_form=questionForm_text()
    return render(request,'app1/post_edit.html',{'form':question_form})

# def post_new_image(request):
#     if request.method =="POST":
#         question_form = questionForm_image(request.POST,request.FILES)
#         if question_form.is_valid():
#             question_form=question_form.save(commit=False)
#             question_form.Question_Image=request.FILES['Question_Image']
#             question_form.save()
#             return redirect('/post/new/byimage/')
#     else :
#         question_form=questionForm_image()
#     return render(request,'app1/post_edit.html',{'form':question_form})

def req_new(request):
    if request.method =="POST":
        form = inputForm(request.POST)
        if form.is_valid():
            subject=form.cleaned_data['Subject']
            topic=form.cleaned_data['topic']
            clas=form.cleaned_data['Class']
            diff=form.cleaned_data['difficulty']
            count=form.cleaned_data['Number_of_Questions']
            return redirect('/post/subject/'+subject+'/'+topic+'/'+clas+'/'+diff+'/'+count)
    else :
        form=inputForm()
    return render(request,'app1/post_input.html',{'form':form})

def post_new_image(request):
    if request.method =="POST":
        question_form = questionForm_image(request.POST,request.FILES)
        if question_form.is_valid():
            image = question_form.cleaned_data['Question_Image']
            im=str(image)
            question_form=question_form.save(commit=False)
            question_form.Question_Image=request.FILES['Question_Image']
            question_form.save()
            return redirect('/post/image/'+im)
    else :
        question_form=questionForm_image()
    return render(request,'app1/post_edit.html',{'form':question_form})

def subject_view(request,Subject,topic,clas,diff,count):
    sublis = question.objects.filter(Subject=Subject,topic=topic, Class=clas).all()
    html='<html><head><script src="https://code.jquery.com/jquery-1.12.3.min.js"></script>'
    html+='<script>'+'var doc = new jsPDF();'
    html+='var specialElementHandlers ='+ '{''#editor'': function (element, renderer) {return true;}};'
    html+='$(''#cmd'').click(function ()'+ '{ doc.fromHTML($("#content").html(), 15, 15,'+' {''width'': 170,''elementHandlers'': specialElementHandlers});doc.save(''sample-file.pdf'');});'
    html+='</script>'
    html+='<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/0.9.0rc1/jspdf.min.js"></script></head><body>'
    html+='<div id="content" style="border-style:solid;border-width: 0px;>'
    html+='<br><h2 style="font-family:verdana;">'+'<center></center>'+'</h2>'
    html+='<br><h2 style="font-family:verdana;">'+'<center>Subject:-'+Subject+'</center>'+'</h2>'
    html+='<h3>'+'<center>Class:-'+clas+'th'+'</center></h3>'
    html+='<p>'+'Time:-3 hours'+'</p><hr>'
    html+='<h4>'+'Instructions:'+'</h4>'
    html+='<h4>'+' &emsp;(i) Answer all '+str(count)+' questions.'+'</h4>'
    html+='<p style="font-style:oblique;">'+' &emsp;(ii) Use of electronic gadgets is not permitted'+'</p>'
    html += '<p style="font-style:oblique;">' + ' &emsp;(iii) Answer of all questions must be neet and clean' + '</p><hr>'
    j=1
    cou=int(count)
    prev=0
    c=0
    questionsforpaper={}
    count=1
    qno=1
    sec=1
    if diff=='Easy':
        easylis=sublis.filter(difficulty='Easy')
        cnt=0
        eas=[]
        eques=int((3*cou)/4)
        if eques!=0:
            html+='<br><h4>'+'<center>'+'Section-'+str(sec)+'</center>'+'</h4>'
            sec=sec+1
            eas=random.sample(range(1,len(easylis)+1),eques)
            eas.sort()
            j=1
            prev=0
            c=0
            html += '<div style="border-style:solid;border-width: 0px; margin-left:50px;>'
            for easylis in easylis:
                if j == eas[prev]:
                    html+='<p style="color:black;">Q'+str(qno)+'. '+easylis.Question+'</p>'
                    #questionsforpaper.update({count,easylis.Question})
                    count=count+1
                    qno=qno+1
                    c=c+1
                    if c==eques :
                        break
                    prev=prev+1
                j=j+1
            html+='</div>'
        cnt=0
        j=1
        prev=0
        c=0
        mques=cou-eques
        mlis=sublis.filter(difficulty='Medium')
        med=[]
        if mques!=0:
            html+='<br><h4>'+'<center>'+' Section-'+str(sec)+'</h4>'
            sec=sec+1
            med=random.sample(range(1,len(mlis)+1),mques)
            med.sort()
            html += '<div style="border-style:solid;border-width: 0px;margin-left:50px;>'
            for mli in mlis:
                if j== med[prev]:
                    html+='<p style="color:black;">Q'+str(qno)+'. '+mli.Question+'</p>'
                    c=c+1
                    qno=qno+1
                    if c==mques :
                        break
                    prev=prev+1
                j=j+1
            html+='</div>'
    else :
        if diff=='Medium':
            cnt=0
            j=1
            prev=0
            c=0
            easylis = sublis.filter(difficulty='Easy')
            eas=[]
            eques=int((2*cou)/5)
            if eques!=0:
                html += '<br><h4>'+'<center>'+' Section-' + str(sec) + '</h4>'
                sec = sec + 1
                eas=random.sample(range(1,len(easylis)+1),eques)
                eas.sort()
                html += '<div style="border-style:solid;border-width: 0px;margin-left:50px;>'
                for easyli in easylis:
                    if j == eas[prev]:
                        html +='<p style="color:black;"> Q'+str(qno)+'. '+ easyli.Question + '</p>'
                        c = c + 1
                        qno=qno+1
                        if c == eques:
                            break
                        prev = prev + 1
                    j = j + 1
                html+='</div>'
            cnt=0
            j=1
            prev=0
            c=0
            mques=eques
            mlis=sublis.filter(difficulty='Medium')
            med=[]
            if mques!=0:
                html += '<br><h4>'+'<center>'+' Section-' + str(sec) + '</h4>'
                sec = sec + 1
                med=random.sample(range(1,len(mlis)+1),mques)
                med.sort()
                html += '<div style="border-style:solid;border-width: 0px;margin-left:50px;>'
                for mli in mlis:
                    if j== med[prev]:
                        html+='<p style="color:black;">Q'+str(qno)+'. '+mli.Question+'</p>'
                        qno=qno+1
                        c=c+1
                        if c==mques :
                            break
                        prev=prev+1
                    j=j+1
                html += '</div>'
            cnt=0
            j=1
            prev=0
            c=0
            hques=cou-(eques+mques)
            hlis=sublis.filter(difficulty='Hard')
            hrd=[]
            if hques!=0:
                html += '<br><h4 >'+'<center>'+' Section-' + str(sec) + '</h4>'
                sec = sec + 1
                hrd=random.sample(range(1,len(hlis)+1),hques)
                hrd.sort()
                html += '<div style="border-style:solid;border-width: 0px;margin-left:50px;>'
                for hli in hlis:
                    if j==hrd[prev]:
                        html+='<p style="color:black;">Q'+str(qno)+'. '+hli.Question+'</p>'
                        c=c+1
                        qno=qno+1
                        if c==hques:
                            break
                        prev=prev+1
                    j=j+1
                html += '</div>'
        else :
            cnt=0
            j=1
            prev=0
            c=0
            easylis = sublis.filter(difficulty='Easy')
            eas=[]
            eques=int(cou/5)
            if eques!=0:
                html += '<br><h4 >'+'<center>'+' Section-' + str(sec) + '</h4>'
                sec = sec + 1
                eas=random.sample(range(1,len(easylis)+1),eques)
                eas.sort()
                html += '<div style="border-style:solid;border-width: 0px;margin-left:50px;>'
                for easyli in easylis:
                    if j == eas[prev]:
                        html += '<p style="color:black;">Q'+str(qno)+'. '+easyli.Question + '</p>'
                        c = c + 1
                        qno=qno+1
                        if c == eques:
                            break
                        prev = prev + 1
                    j = j + 1
                html += '</div>'
            cnt=0
            j=1
            prev=0
            c=0
            mques=int((3*cou)/10)
            mlis=sublis.filter(difficulty='Medium')
            med=[]
            if mques!=0:
                html += '<br><h4 >'+'<center>'+' Section-' + str(sec) + '</h4>'
                sec = sec + 1
                med=random.sample(range(1,len(mlis)+1),mques)
                med.sort()
                html += '<div style="border-style:solid;border-width: 0px;margin-left:50px;>'
                for mli in mlis:
                    if j== med[prev]:
                        html+='<p style="color:black;">Q'+str(qno)+'. '+mli.Question+'</p>'
                        c=c+1
                        qno=qno+1
                        if c==mques :
                            break
                        prev=prev+1
                    j=j+1
                html += '</div>'
            cnt=0
            j=1
            prev=0
            c=0
            hques=cou-(eques+mques)
            hlis=sublis.filter(difficulty='Hard')
           # html+=str(eques)+' '+str(mques)+' '+str(hques)
            hrd=[]
            if hques!=0 :
                html += '<br><h4 >'+'<center>'+' Section-' + str(sec) + '</h4>'
                sec = sec + 1
                hrd=random.sample(range(1,len(hlis)+1),hques)
                hrd.sort()
                html += '<div style="border-style:solid;border-width: 0px;margin-left:50px;>'
                for hli in hlis:
                    if j==hrd[prev]:
                        html+='<p style="color:black;">Q'+str(qno)+'. '+hli.Question+'</p>'
                        c=c+1
                        qno=qno+1
                        if c==hques:
                            break
                        prev=prev+1
                    j=j+1
                html+='</div>'
    html+='<br><br><p><center>------------Paper ends------------</center></p><hr><br>*For Downloading this as a PDF press Ctrl+P</div></body></html>'
    return HttpResponse(html)
    #return render(request,'app1/papergenerated.html',html)

def image_Text(request,url):
    ########### Python 2.7 #############
    import httplib, urllib, base64, time, json

    ###############################################
    #### Update or verify the following values. ###
    ###############################################

    # Replace the subscription_key string value with your valid subscription key.
    subscription_key = 'a265e42ee7b74e15b26983d5b7cc49de'

    # Replace or verify the region.
    #
    # You must use the same region in your REST API call as you used to obtain your subscription keys.
    # For example, if you obtained your subscription keys from the westus region, replace
    # "westcentralus" in the URI below with "westus".
    #
    # NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
    # a free trial subscription key, you should not need to change this region.
    uri_base = 'westcentralus.api.cognitive.microsoft.com'

    headers = {
        # Request headers.
        # Another valid content type is "application/octet-stream".
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key,
    }

    # The URL of a JPEG image containing handwritten text.
    body = "{'url':'"+url+"'}"

    # For printed text, set "handwriting" to false.
    params = urllib.urlencode({'handwriting': 'true'})

    try:
        # This operation requrires two REST API calls. One to submit the image for processing,
        # the other to retrieve the text found in the image.
        #
        # This executes the first REST API call and gets the response.
        conn = httplib.HTTPSConnection(uri_base)
        conn.request("POST", "/vision/v1.0/RecognizeText?%s" % params, body, headers)
        response = conn.getresponse()

        # Success is indicated by a status of 202.
        if response.status != 202:
            # Display JSON data and exit if the first REST API call was not successful.
            parsed = json.loads(response.read())
            conn.close()
            exit()

        # The 'Operation-Location' in the response contains the URI to retrieve the recognized text.
        operationLocation = response.getheader('Operation-Location')
        parsedLocation = operationLocation.split(uri_base)
        answerURL = parsedLocation[1]

        # NOTE: The response may not be immediately available. Handwriting recognition is an
        # async operation that can take a variable amount of time depending on the length
        # of the text you want to recognize. You may need to wait or retry this GET operation.
        time.sleep(2)

        # Execute the second REST API call and get the response.
        conn = httplib.HTTPSConnection(uri_base)
        conn.request("GET", answerURL, '', headers)
        response = conn.getresponse()
        data = response.read()

        # 'data' contains the JSON data. The following formats the JSON data for display.
        parsed = json.loads(data)
        x= json.dumps(parsed, sort_keys=True, indent=2)
        conn.close()

    except Exception as e:
        x=e
    return render(request,'app1/convert.html',{'x':x})