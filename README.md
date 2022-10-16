# بايثون بطيئة! كيف تجعلها أسرع لـ 453 مليون عملية في الثانية؟ تعلم Cython Numba PyPy  الآن
 

<h2 align="right">المصادر والأكواد والروابط الخاصة بالحلقة </h2>

[![شاهد الفيديو](https://i.ytimg.com/vi/GKlWmNsATFc/maxresdefault.jpg)](https://youtu.be/GKlWmNsATFc)

[![مجتع بايثون العربي](https://images.milled.com/2019-12-19/3pGli9s5cCGeONOJ/uM1ZG0_8Y8E8.gif)](https://www.youtube.com/channel/UC9ocsRoOwj9tkAQNfUt8ZJg?sub_confirmation=1)

<p align="right">
بايثون بطيئة!؟ وهل يمكن جعلها أسرع؟ 🤫 إليك السر!
معروف أن بايثون إنها لُغةٌ سهلة التعلم، لكنها صعبةُ الإتقان وأروع لغة برمجة على الإطلاقِ. يقول البعض، ينال منها عيب خطيرٌ يُهدد وجودها ويسير بها نحو الفناء فمسألة البطء والسرعة في لغة بايثون مشكلة جليلة لا يمكن للمبرمج غض البصر عنها والبعض الآخر يراها فوق الفناء والزوال فهي وُجدت لتُحَب رغم عيوبها... ويبقى الفريقان في جدل مستمر !
كلامهم صحيح نوعا ما، إلّا أننا نستطيع جعلها أسرع لتنجز نصف مليار عملية في الثانية!

جدلٌ جئنا اليوم كي نقوم بحسمه للأبد! لقد حان الوقت لوضع لغة بايثون رهن التحقيق، لإزالة الغموض عن أسوء شُبهتين وأخطرهما في عالم لغات البرمجة على الإطلاق. ألا وهما الآداءُ السيء والبطء!  !

في الفيديو أعلاه، ستتعرفون عن قربٍ على التصميم الداخلي للغة بايثون:
* كيف يتأثر  الآداء؟
* ما الذي يحصل وراء الكواليس؟
* كيف تعمل لغة بايثون؟
* ما طبيعة العلاقة بينها وبين لغة السي؟  

ونحن نجيب عن هذه الأسئلة، ستتعرفون على الـCompiler والـInterpreter وعلى الرحلة التي يقطعها كودك البرمجي ليصبح لغة الآلة ويخاطب مُعالجات الكومبيوتر، إضافة إلى الـdynamic typing(تلقائية التعرف على البيانات)  والـmultiprocessing (تعدد المعالَجات)، إلى أن نجعل لغة بايثون أسرع بآلاف المرات بالإستعانة بـأي من هذه المكتبات:
* Cython
* Numba
* PyPy

وصدقنا إن أخبرناك بأن هذا الشرح سيكون صديقاً للمبتدئين beginner friendly! 
</p>
 
# كود بايثون المستخدم في الشرح

### يُفضل تحميل الأكواد الموجودة أعلاه في المستودع بدل نسحها ولصقها فأسماء الملفات مهمة.

## Vanilla Python


```python
def prime_py(range_start, range_end):
	count_of_primes = 0
	range_start = range_start if range_start >= 2 else 2
	for num in prange(range_start, range_end + 1):
		for div_num in prange(2, num):
			if ((num % div_num) == 0):
				break
		else:
			count_of_primes += 1

	return count_of_primes
```
# فقرة استخدام Cython
### أولاً تثبيت Cython

<!-- <h2 >Install cython </h2> -->
<p align="right">
 بداية تثبيت حزمة cython:
</p>

## Linux/Ubuntu

```bash
pip3 install cython
```
وأدوات البناء C/C++ (ضرورية)
```bash
sudo apt-get install build-essential
```
[شرح مصور من اليوتيوب](https://youtu.be/GKlWmNsATFc?t=900)

## Windows

```cmd
python -m pip install cython
```

يجب عليك تثبيت MinGW الذي يحتوي مترجمات لغة السي من هنا [SourceForge](https://sourceforge.net/projects/mingw/)

الخطوة التالية ضرورية جداً، يجب إضافة مسار مجلد Bin من البرنامج إلى مسارات البيئة  في نظام الويندوز، الأمر سهل، إذهب الى Start  واكتب Environment Variables واختر هذه الأيقونة، ثم أنقر على Environment Variables، هنا في الأسفل إبحث عن متغير PATH ثم أضف إليه مسار مجلد Bin واعمل حفظ. 
<!-- لا أصدق أنني أضطر لشرح هذه الأشياء لكم بالتفصيل ! -->

[شرح مصور من اليوتيوب](https://youtu.be/GKlWmNsATFc?t=923)

## Mac OS

```bash
pip3 install cython
```



تحميل أدوات المطورين XCode developer tools عبر 
تثبيت  إضافة Command Line Tools
يجب تثبيت xcode أولا وبعدها وافق على تنصيت الـ Command Line Tools والأمور تمام
```bash
sudo xcode-select --install
```
[شرح مصور من اليوتيوب](https://youtu.be/GKlWmNsATFc?t=906)



المهم بعد تثبيت مترجم لغة السي أياً كان نظام تشغيلك، قم بالتأكد من أنه يعمل عبر كتابة الأمر التالي :
```bash
gcc –version
```
إذا ظهر لك اصدار المُترجِم فالأمورُ تمام.
<!-- وإلا فإنني لم أعد صديقك لأنك على الأرجح لم تطبق الشرح كما فصّلت، أمزح أنت صديقي ولكن ليس جداً، دعنا نحافظ على علاقتنا هكذا .. -->


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
*تنبيه : يجب أن يكون ملف Primes_cython موجود في نفس مجلد الكود*

# فقرة Numba 
### تثبيت Numba

```bash
pip install numba
```

*من [الوثائق الرسمية لـ numba](https://numba.pydata.org/)*

تقوم Numba بترجمة الوظائف المكتوبة بلغة بايثون إلى لغة الآلة في وقت التشغيل، باستخدام مترجِم يُدعى الـ LLVM.
هذا المُترجم يلتقط الدوال من الـ bytecode قبل أن تذهب إالى المُفسّر الخاص بلغة بايثون ويحولها إلى كود آلة أصلي بلمح البصر ليتم تنفيذها على المعالج مباشرة.

---
وسرعة هذا المترجِم يُمكن أن تُضاهي سرعة لغتي السي والفورتران، بخلاف الحلول الأخرى مع نامبا لست بحاجة إلى استبدال مترجم Python أو تشغيل خطوة ترجمة منفصلة أو حتى تثبيت مترجم  السي، فقط قم بتثبيت المكتبة وإضافة المؤثِت Decorator إلى الكود، ونامبا تقوم بالباقي !
لا يوجد أسهل من هذا، أبداً، تابع التجربة والشرح الموجود في الفيديو على اليوتيوب..


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
<h2>Numba Prange </h2>


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

# فقرة PyPy
### تثبيت باي بايPyPy

إذن كما هو معلوم PyPy يمكن اعتباره توزيعة مختلفة من بايثون، نقوم بتحميله من

 [التحميل من موقعه الرسمي](https://www.pypy.org/)  

 نقوم بفك الضغط ووضعه في مجلد في مكان ما بحاسبنا، أنا أفضل القرص سي
نذهب إلى الـ envirenement path ونضيف مسار المجلد إليه
إذن الآن إذا كتبنا pypy في مسطّر الأوامر، يجب أن يعمل مثل بايثون



> تذكير : الأكواد موجودة في المستودع، والفيديو على اليوتيوب يشرح كل شيء .

<h1 align="right">أتمنى أن نحصل على المزيد من الرعاية والدعم لنتمكن من توفير المزيد من الحلقات الغنية، أيضاً يمكنكم دعمنا بـ 5 دولار عبر زر شكراً الموجود قرب زر الإعجاب بالحلقة في اليوتيوب

https://youtu.be/GKlWmNsATFc

تذكروا أن كل مساهماتكم ستبقى صدقةً جارية للعلم في هذه القناة، تذكروا كذلك أن تعليقاتكم مهمة جداً كي تصِل الحلقة إلى أكبر عدد ممكن من الناس، لا تترددوا في نشر الحلقة إنها عبارة عن مادة علمية خالية من كل المخالفات، تحياتي
</h1>
