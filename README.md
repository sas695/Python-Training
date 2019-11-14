<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h1>Programming Assignment 2: Password Cracking</h1>
<ul>
<li>Fundamentals of Modern Software - Fall 2019</li>
<li>Due September 18 by 11:59 PM</li>
</ul>
<h2>Introduction</h2>
<p>The goals of this assignment are:</p>
<ol>
<li>To ensure that you are familiar with strings, lists, and for and while loops.</li>
<li>To start familiarizing you with reading command-line arguments and files.</li>
<li>To give you practice working with data sets too big to process by hand.</li>
</ol>
<p><strong>REMINDERS</strong></p>
<ol>
<li><strong>When you are done, be sure to submit your work.</strong></li>
<li><strong>You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.</strong></li>
<li><strong>Be sure to test your programs thoroughly on a wide range of inputs. We will.</strong></li>
<li><strong>Your programs' output should match the output in the samples EXACTLY, to the letter. We will grade your work in part using automated tests, and as you have seen, even a single-character difference can cause a comparison not to match.</strong></li>
<li><strong>We have provided you with 'stub' programs that you can &ndash; and should &ndash; use as a starting pont.</strong></li>
</ol>
<p><em>This assignment is based on a problem from the Georgetown Computer Programming for Lawyers course.</em></p>
<p><em>Although the steps we are teaching you below are stylized and simplified, we are teaching you a key skill used for evil by computer criminals and for good by computer security professionals. We urge you to use these new skills only for good. If you need another reason to listen to this advice, the unauthorized use of another person's password can be a federal crime.</em></p>
<h2>Background</h2>
<p>You have been retained by the (fictitious) website Concerto to help secure its systems. You will implement a feature that lets users protect their accounts with a password.  Then you will help Concerto check whether its users are picking good passwords.</p>
<p>Concerto could (but does not) store its passwords in a &ldquo;plaintext&rdquo; file like <code>potter_plaintext.txt</code> (each line consists of <code>&lt;username&gt;:&lt;password&gt;</code>):</p>
<pre><code>draco:DAGRON
hermione:hermione
luna:Quibbler
ludo:tournament
hagrid:creatures
albus:albus
</code></pre>
<p>This woud be horribly insecure, because if a hacker managed to get a copy of the plaintext password file, he or she could log in as any user. Instead, Concerto  &ldquo;hashes&rdquo; its passwords before storing them by running them through a function <code>hash()</code> which scrambles them into 32-character strings. Here is a file, <code>potter_hashed.txt</code>, but with the passwords hashed:</p>
<pre><code>draco:8aefe1be72fb351dfe1c5a364bb3a092
hermione:45a866e5332348a12d1602883602eeed
luna:f9908a895120dcfa36e0f008b00f4920
ludo:8df358eebbbb64bf19235a902db73505
hagrid:f9c1d2a06a6defe56386ae930f3827e3
albus:66af4de17f60f37e08eb8ff07310b466
</code></pre>
<p>The hashes have three nice properties. Frist, they look random: they follow no discernable pattern. Second, they are consistent: <code>hash('creatures')</code> is always <code>'f9c1d2a06a6defe56386ae930f3827e3'</code>. And third, it is extremely hard to reverse: even if you know that <code>hash(password) == 'f9c1d2a06a6defe56386ae930f3827e3'</code>, you are no closer to knowing that <code>password == 'creatures'</code>.</p>
<p>Whenever a user tries to log in, Concerto takes the hash of the password the user typed in and checks whether it matches the hash of the actual password. In other words, it tests whether <code>hash(guessedPassword) == hash(actualPassword)</code>. This way, the Concert Hell only ever needs to store <code>hash(actualPassword)</code> rather than <code>actualPassword</code> itself.</p>
<p>We have provided you with a Python file, <code>hash.py</code> ,that implements <code>hash()</code> using a specific hash function called <a href="https://en.wikipedia.org/wiki/MD5">MD5</a>. It can be used in two different ways. First, you can run it from the command line to hash a single password:</p>
<pre><code>$ python hash.py hello
5d41402abc4b2a76b9719d911017c592
</code></pre>
<p>You can also use <code>import</code> so that you can access the hash function from your own program. As long as <code>hash.py</code> is in the same directory as your program, you can  add the line <code>import hash</code> to the beginning of your program. After that, you can call <code>hash.hash()</code> as desired:</p>
<pre><code>&gt;&gt;&gt; import hash
&gt;&gt;&gt; hash.hash('hello')
'5d41402abc4b2a76b9719d911017c592'
</code></pre>
<p>You may also find the <code>.split()</code> function useful in parsing password files. As a reminder:</p>
<pre><code>&gt;&gt;&gt; s = 'yes,yes,no'
&gt;&gt;&gt; s.split(',')
['yes', 'yes', 'no']
</code></pre>
<h2>login.py</h2>
<p>Write a program that takes one command-line argument: the name of a hashed <em>password file</em>.  When run, the program prompts the user to enter a username and a password.  If the password is correct, it prints a confirmation.  If the username does not exist, or the password is incorrect, the program should print an error message and prompt the user to try again.  After five failed login attempts, the program should tell the user they have tried too many times and quit.</p>
<pre><code>$ python login.py potter_hashed.txt
Username: hermione
Password: hermione
Password correct. Welcome!
$ python login.py potter_hashed.txt
Username: myrtle
Password: ooooo
Incorrect username/password. Try again.
Username: myrtle
Password: ooooo
Incorrect username/password. Try again.
Username: draco
Password: asdf1234
Incorrect username/password. Try again.
Username: draco
Password: DRAGON
Incorrect username/password. Try again.
Username: albus
Password: creatures
Incorrect username/password.
Too many failed login attempts. Sorry.
$ python login.py potter_hashed.txt
Username: hagrid
Password: creatures   
Password correct. Welcome!
</code></pre>
<h2>cracker1.py</h2>
<p>Write a program that takes one command-line argument: the name of a hashed <em>password file</em>. It should print a list of the usernames of the users whose password is the same as their username, one username per line, in the same order they appear in the password file.</p>
<pre><code>$ python cracker2.py potter_hashed.txt
hermione
albus
</code></pre>
<p><em>Hint: Start by copying your code from <code>login.py</code> and then modify it so that it performs the required analysis.</em></p>
<h2>cracker2.py</h2>
<p>Write a program that takes two command-line arguments: the name of a hashed <em>password file</em> and the name of a a <em>dictionary file</em> containing a list of words, one per line. It should output a list of lines of the form <code>&lt;username&gt;:&lt;password&gt;</code>, one line for each user whose password appears in the dictionary file, sorted in alphabetical order by username.</p>
<pre><code>$ python cracker2.py potter_hashed.txt words.txt
hagrid:creatures
ludo:tournament
</code></pre>
<p><em>Hint: Start by copying your code from <code>cracker1.py</code> and then modify it so that it uses the dictionary file, too. Try not to read the dictionary file more than once.</em></p>
</div>