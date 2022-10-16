# بايثون بطيئة! كيف تجعلها أسرع لـ 453 مليون عملية في الثانية؟ تعلم Cython Numba PyPy  الآن
 

<h2 align="right">المصادر والأكواد والروابط الخاصة بالحلقة </h2>

[![شاهد الفيديو](https://i.ytimg.com/vi/GKlWmNsATFc/maxresdefault.jpg)](https://youtu.be/GKlWmNsATFc)

[![مجتع بايثون العربي](https://images.milled.com/2019-12-19/3pGli9s5cCGeONOJ/uM1ZG0_8Y8E8.gif)](https://www.youtube.com/channel/UC9ocsRoOwj9tkAQNfUt8ZJg?sub_confirmation=1)

<p align="right">
بايثون بطيئة! هي يمكن جعلها أسرع؟ إنها لُغةٌ سهلة التعلم، لكنها صعبةُ الإتقان 🤫 سوف يذهلك هذا السر !
بايثون إنها أروع لغة برمجة على الإطلاقِ -يقول البعض- لولا عيبٌ خطيرٌ يُهدد وجودها ويسير بها نحو الفناء ، البعض الآخر يراها فوق الفناء والزوال فهي وُجدت لتُحَب رغم عيوبها .. وسيبقى الفريقان في جدل مستمر !
فريق يرى مسألة البطء والسرعة في لغة بايثون مشكلة عظيمة لا يمكن للمبرمج غض البصر عنها ، وفريق يقول : بايثون لغة برمجة بطيئة! نعم ولكن لا يهم لأننا نستطيع جعلها أسرع لـ نصف مليار عملية في الثانية !

جدلٌ جئنا اليوم كي نقوم بحسمه للأبد ، فلقد حان الوقت لوضع لغة بايثون رهن التحقيق ، لإزالة الغموض عن أسوء شُبهةٍ وأخطر تُهمة في عالم لغات البرمجة على الإطلاق : الآداءُ السيء والبطء ! اليوم ستشاهدون واحدة من أفضل حلقات البرنامج !

في  هذه الحلقة سنتعرف عن قربٍ على التصميم الداخلي للغة بايثون ، كيف يؤثر على الآداء، ما الذي يحصل في الكواليس، وكيف تعمل لغة بايثون؟، وما طبيعة العلاقة بينها وبين لغة السي ؟!  

خلال كل هذا ستتعرف على الـ Compiler و الـ Interpreter وعلى الرحلة التي يقطعها الكود الخاص بك ليصل إلى لغة الآلة ويخاطب مُعالجات الكومبيوتر ، سنتعرف على الـ  dynamic typing  والـ multiprocessing ، والأهم وهو أهم شيء على الإطلاق : 

كيف تجعل لغة بايثون أسرع ؟ بآلاف المرات ، وستتضمن الحلقة شرحا  عمليا لـ Cython و Numba و PyPy ، والكثير من المواضيع المهمة الأخرى ، وصدقني أيضا إذا أخبرتك بأن هذا الشرح سيكون صديقاً للمبتدئين beginner friendly  ! 

 </p>
<h2 align="right">الكود الذي سنستخدمه في الشرح </h2>
<h3 align="right">يُفضل تحميل الأكواد الموجودة أعلاه في المستودع بدل استخدم النسح واللصق لتفادي الأخطاء لأن أسماء الملفات مهمة . </h3>

<h2 >Vanilla Python </h2>


```python
def  prime_py(range_start, range_end):
	count_of_primes =  0
	range_start = range_start if range_start >=  2  else  2
	for num in prange(range_start, range_end +  1):
		for div_num in prange(2, num):
			if ((num % div_num) ==  0):
				break
		else:
			count_of_primes +=  1

	return count_of_primes
```

<h2 align="right">تثبيت سايثون Cython </h2>

<h2 >Install cython </h2>

<div align="right">
  بداية سنقوم بتثبيت حزمة Cython ، يمكن تثبيته مثل أي مكتبة بايثون عبر مدير الحُزم عن طريق كتابة الأمر التالي :

    python -m pip install cython


<h3 align="right">تثبيت cython على أوبنتو </h3>
الآن لتنصيب GCC ، أولاً إذا كنت تستخدم إحدى توزيعات يوبنتو ubuntu أو دِبيان Debian قم تنفيذ الأمر التالي :

    $ sudo apt-get install build-essential
 
[شرح مصور من اليوتيوب](https://www.youtube.com/watch?v=QKUhMOd-KOM)


 <h3 align="right">تثبيت cython على الماكنتوش</h3>
أما إذا كنت تستخدم نظام الماكنتوش فيمكنك الحصول عليه عن طريق أدوات المطورين XCode developer tools عبر 
تثبيت  إضافة Command Line Tools
يجب تثبيت xcode أولا وبعدها وافق على تنصيت الـ Command Line Tools والأمور تمام
 
[شرح مصور من اليوتيوب](https://www.youtube.com/watch?v=wY24ehH6mC0)

 
<h3 align="right">تثبيت cython على الويندوز</h3>

[تحميل mingw](https://sourceforge.net/projects/mingw/)

وأخيراً إذا كنت تستخدم أحد أنظمة الويندوز فإنه يجب عليك تثبيت MinGW الذي يحتوي مترجمات لغة السي ، الأمر بسيط
 ،إبحث في جوجل عن  MinGW64، بعد تحميله من موقع سورسفورج sourceforge إتبع الخطوات التالية وفي الأخير تأكد من ملء اختيار GCC G++ و mingw base ثم أعمل Apply changes وأخير Apply  وانتظار انتهاء التثبيت .

الخطوة التالية ضرورية جداً ، يجب إضافة مسار مجلد Bin من البرنامج إلى مسارات البيئة  في نظام الويندوز ، الأمر سهل ، إذهب الى Start  واكتب Environment Variables واختر هذه الأيقونة  ، ثم أنقر على Environment Variables ، هنا في الأسفل إبحث عن متغير PATH ثم أضف إليه مسار مجلد Bin واعمل حفظ ، لا أصدق أنني أضطر لشرح هذه الأشياء لكم بالتفصيل !

المهم بعد تثبيت مترجم لغة السي أياً كان نظام تشغيلك ، قم بالتأكد من أنه يعمل عبر كتابة الأمر التالي :

    gcc –version

إذا ظهر لك اصدار المُترجِم فالأمورُ تمام ، وإلا فإنني لم أعد صديقك لأنك على الأرجح لم تطبق الشرح كما فصّلت ، أمزح أنت صديقي ولكن ليس جداً ، دعنا نحافظ على علاقتنا هكذا ..
<h2 >Cython .Pyx Code</h2>

```python
def prime_py(int range_start, int range_end):
    cdef int count_of_primes = 0
    cdef int num
    cdef int div_num
	range_start = range_start if range_start >=  2  else  2
	for num in prange(range_start, range_end +  1):
		for div_num in prange(2, num):
			if ((num % div_num) ==  0):
				break
		else:
			count_of_primes +=  1

	return count_of_primes
```

<h2 >Cython import Code</h2>

```python
import pyximport; pyximport.install()

from Primes_cython import prime_py

print(prime_py(0,100000))
```
<p align="right">
تنبيه : يجب أن يكون ملف Primes_cython موجود في نفس مجلد الكود
</p>
<h2 >Numba </h2>
<h2 align="right">تثبيت Numba</h2>
<h3 >Install Numba</h3>

    pip install numba
[الثوثيق الرسمي لـ numba](https://numba.pydata.org/)
تقوم Numba بترجمة الوظائف المكتوبة بلغة بايثون إلى لغة الآلة في وقت التشغيل ، باستخدام مترجِم يُدعى الـ LLVM.
هذا المُترجم يلتقط الدوال من الـ bytecode قبل أن تذهب إالى المُفسّر الخاص بلغة بايثون ويحولها إلى كود آلة أصلي بلمح البصر ليتم تنفيذها على المعالج مباشرة .
وسرعة هذا المترجِم يُمكن أن تُضاهي سرعة لغتي السي والفورتران، بخلاف الحلول الأخرى مع نامبا لست بحاجة إلى استبدال مترجم Python أو تشغيل خطوة ترجمة منفصلة أو حتى تثبيت مترجم  السي ، فقط قم بتثبيت المكتبة وإضافة المؤثِت Decorator إلى الكود، ونامبا تقوم بالباقي !
لا يوجد أسهل من هذا ، أبداً ، تابع التجربة والشرح الموجود في الفيديو على اليوتيوب..


```python
from numba import jit

@jit()
def  prime_py(range_start, range_end):
	count_of_primes =  0
	range_start = range_start if range_start >=  2  else  2
	for num in prange(range_start, range_end +  1):
		for div_num in prange(2, num):
			if ((num % div_num) ==  0):
				break
		else:
			count_of_primes +=  1

	return count_of_primes
```
<h2 >Numba Prange </h2>


```python
from numba import jit , prange

@jit(parallel=True)
def  prime_py(range_start, range_end):
	count_of_primes =  0
	range_start = range_start if range_start >=  2  else  2
	for num in prange(range_start, range_end +  1):
		for div_num in prange(2, num):
			if ((num % div_num) ==  0):
				break
		else:
			count_of_primes +=  1

	return count_of_primes
```




<h2 align="right">تثبيت باي بايPyPy</h2>
<h2 >Install PyPy</h2>
إذن كما هو معلوم PyPy يمكن اعتباره توزيعة مختلفة من بايثون ، نقوم بتحميله من

 [التحميل من موقعه الرسمي](https://www.pypy.org/)  

 نقوم بفك الضغط ووضعه في مجلد في مكان ما بحاسبنا ، أنا أفضل القرص سي
نذهب إلى الـ envirenement path ونضيف مسار المجلد إليه
إذن الآن إذا كتبنا pypy في مسطّر الأوامر ، يجب أن يعمل مثل بايثون

</div>

> تذكير : الأكواد موجودة في المستودع ، والفيديو على اليوتيوب يشرح كل شيء .

<h1 align="right">
، أتمنى أن نحصل على المزيد من الرعاية والدعم لنتمكن من عمل المزيد من الحلقات الثرية ، أيضاً يمكنكم دعمنا بـ 5 دولار عبر زر شكراً الموجود أسفل الحلقة في اليوتيوب، تذكروا أن كل مساهماتكم ستبقى صدقةً جارية للعلم في هذه القناة ، تذكروا كذلك أن تعليقاتكم مهمة جداً كي تصِل الحلقة إلى أكبر عدد ممكن من الناس ، لا تتردد في نشر الحلقة إنها عبارة عن مادة علمية خالية من كل المخالفات ، تحياتي
 </h1>
