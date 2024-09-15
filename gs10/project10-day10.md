        from django.shortcuts import render
        from datetime import datetime
        # Create your views here.
    
    ## view function for path('cor/learndj/')

        def learn_django(request):
            cname = 'Django'
            duration = '4 Months'

            seats = 10
            django_Details = {'n':cname,'du':duration,'st':seats}

            return render(request,'course/courseone.html',context=django_Details)
        ### courseone.html
                    
                {% comment %} |upper in {{n | upper}} will make all the character capital of the value of the n variable {% endcomment %}
                <h1>Course name: {{n | upper}}, Duration of cpurse : {{du}}, total alowed seats : {{st}}</h1>

        ## view function for path('cor/learnpy/')

        def learn_python(request):
            return render(request,'course/coursetwo_with_filter.html',{'nm':'this course iMMMMMMMs awesome'})

        ###  coursetwo_with_filter.html.html
            <h1>Course name: {{nm | capfirst}}</h1>         {% comment %} capfirst will capitalize the first letter capital {% endcomment %}
            <h1>Course name: {{du| default:"nothing ==>this means no dictionary is passed from view or dictionary ky value is false"}}</h1>
            <h1>Course name: {{nm | length}}</h1>
            <h1>Course name: {{nm | lower}}</h1>
            <h1>Course name: {{nm |slice:'7' }}</h1>    {% comment %} slice will make slice from start upto the given number of characters {% endcomment %}
            <h1>Course name: {{nm |truncatechars:'7' }}</h1>    {% comment %} truncatechars will make slice from start upto the given number of characters and  will not show the last chracter but wil show ... {% endcomment %}
            <h1>Course name: {{nm |truncatewords:'2' }}</h1>    {% comment %} truncatewords will make slice from start upto the given number of words and wil show ... by default {% endcomment %}


        ##  view for path('cor/dt/')
        
        def showing_date_time_template(request):
            d = datetime.now()

            return render(request,'course/date_time_template.html',{'dt':d})

        ### date_time_template.html
            {{dt | date:'D d M Y'}}                    {% comment %} Sun 15 Sep 2024 {% endcomment %}
            <br>
            {{dt| time:'H:i'}}                         {% comment %} 22:19 {% endcomment %}
            <br>
            {{dt | date:'SHORT_DATE_FORMAT'}}          {% comment %} 09/15/2024 {% endcomment %}
            <br>
            {{dt | time:'TIME_FORMAT'}}                {% comment %} 10:19 p.m.{% endcomment %}
            <br> 
            {{dt}}                                     {% comment %} Sept. 15, 2024, 10:19 p.m.{% endcomment %}

            
        
        ## view function for path('cor/numformat/')
        def filter_for_float__number_format(request):
            return render(request,'course/float_number_formate.html',{'p1':56.24321, 'p2':56.0000, 'p3':56.37000}) 
        ### float_number_formate.html

                <h2>Example 1</h2>
                <h3>{{p1}}</h3>
                <h3>{{p2}}</h3>
                <h3>{{p3}}</h3>

                <h2>Example 2</h2>
                <h3>{{p1|floatformat}}</h3>
                <h3>{{p2|floatformat}}</h3>
                <h3>{{p3|floatformat}}</h3>


                <h2>Example 3</h2>
                <h3>{{p1|floatformat:3}}</h3>
                <h3>{{p2|floatformat:3}}</h3>
                <h3>{{p3|floatformat:3}}</h3>

                <h2>Example 4</h2>
                <h3>{{p1|floatformat:0}}</h3>
                <h3>{{p2|floatformat:0}}</h3>
                <h3>{{p3|floatformat:0}}</h3>

                <h2>Example 5</h2>
                <h3>{{p1|floatformat:-3}}</h3>
                <h3>{{p2|floatformat:-3}}</h3>
                <h3>{{p3|floatformat:-3}}</h3>


        ## view for how to use is and else in django template
        def if_st(request):
            # return render(request,'course/if_st.html',{'name':'True'}) #will not show anything if we pass false value
            # return render(request,'course/if_st.html',{'name':'Django'})
            # return render(request,'course/if_st.html',{'name':'Django', 'st':5})
            return render(request,'course/if_st.html',{'name':'Django',})
        ### if_st.html
                    
                {% if name  %}
                
                <h1>Course name =  {{name}}</h1>
                
                {% endif %}


                {% if name and st %}
                <h3>{{st}} seats re aaliable for {{name}} course</h3>
                {% endif %}

                {% if name or st %}
                <h3>{{st}} seats re aaliable for {{name}} course</h3>
                {% endif %}

                {% if not st %}
                <h3> no seats are avaliable for {{name}} course</h3>
                {% endif %}

                {% if name == 'Django' and st == 5 %}
                <h3>{{st}} seats re aaliable for specific {{name}} course</h3>
                {% endif %}

                {% if name|length > 4 %}
                <p>character in django word is greater than 4</p>
                {% endif %}
            
                {% if name|length > 9 %}
                <h1> if condition</h1>
                {% elif not st %}
                <h2>no seat avalible</h2>
                {% else %}
                <h2> hefe i used else condition</h2>
                {% endif %}

        ## how to use loops in Django templates
        def loops(request):
            student = {'names': ['rahim','nasir','ibrahim']}
            return render(request,'course/for_loop.html',context = student)
        ### for_loop.html

            {% comment %}  {% for name in names reversed  %}  if we want in reversed order {% endcomment %}
            {% for name in names  %}
            <li>{{name}}</li>
            {% empty %}
            <h3>when nothing is passed this message will show </h3>
        ##  how to use forloop
        def forloop_varaibles(request):
            student = {'names': ['rahim','nasir','ibrahimend']}

            return render(request,'course/forloop_varaibles.html',student)

            forloop_varaibles.html
                {% for name  in names  %}
                {{forloop.counter}} {{name}} 
                    <br>
                    {% endfor %}
                <hr>

                {% for name  in names  %}
                {{forloop.counter0}} {{name}} 
                <br>
                {% endfor %}
                <hr>
                    {% for name  in names  %}
                    {{forloop.revcounter}} {{name}} 
                    <br>
                    {% endfor %}
                <hr>
                {% for name  in names  %}
                {{forloop.revcounter0}} {{name}} 
                <br>
                {% endfor %}

                <hr>
                {% for name  in names  %}
                {{forloop.first}} {{name}} 
                <br>
                {% endfor %}

                <hr>
                {% for name  in names  %}
                {{forloop.last}} {{name}} 
                <br>
                {% endfor %}


        ## how to use nested dictionary in django template
        def nested_loop_and_dict(request):
            stu = { 'stu1' : {'name': "rahim",'age':1},
                    'stu2' : {'name': "israr",'age':2},
                    'stu3' : {'name': "faizan",'age':3},

                }
            
            students = {'student': stu}
            
            return render(request,'course/nested_dict_and_for.html',students)

        ### nested_dict_And_for.html
                {{student}}
                <hr>
                {{student.stu1}}
                {{student.stu2}}
                {{student.stu3}}
                <hr>
                {{student.stu1.name}}
                {{student.stu1.age}}
                <hr>
                {{student.stu2.name}}
                {{student.stu2.age}}
                <hr>
                {{student.stu3.name}}
                {{student.stu3.age}}

                {{data}}


                {% comment %} or through the following way {% endcomment %}

                <hr>
                {% for key,value in data.items  %}
                
                {{key}} = {{value}}
                <br>
                {% endfor %}

            {% comment %} Another way {% endcomment %}
                <hr>
                {% for key,value in data.items  %}
                {{key}} = {{value}} <br>

                {% for key,value in value.items  %}
                
                {{forloop.parentloop.counter}}--{{key}} = {{value}}
                <br>
                {% endfor %}
                <br>
                {% endfor %}

        

        def passing_key_value(request):
            data = { 'stu1' : {'name': "rahim",'age':1},
                        'stu2' : {'name': "israr",'age':2},
                        'stu3' : {'name': "faizan",'age':3},

                    }
            
            return render(request,'course/nested_dict_and_for.html',{'data':data})
            