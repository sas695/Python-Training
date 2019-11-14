<style type="text/css">.rendered-markdown{font-size:14px} .rendered-markdown>*:first-child{margin-top:0!important} .rendered-markdown>*:last-child{margin-bottom:0!important} .rendered-markdown a{text-decoration:underline;color:#b75246} .rendered-markdown a:hover{color:#f36050} .rendered-markdown h1, .rendered-markdown h2, .rendered-markdown h3, .rendered-markdown h4, .rendered-markdown h5, .rendered-markdown h6{margin:24px 0 10px;padding:0;font-weight:bold;-webkit-font-smoothing:antialiased;cursor:text;position:relative} .rendered-markdown h1 tt, .rendered-markdown h1 code, .rendered-markdown h2 tt, .rendered-markdown h2 code, .rendered-markdown h3 tt, .rendered-markdown h3 code, .rendered-markdown h4 tt, .rendered-markdown h4 code, .rendered-markdown h5 tt, .rendered-markdown h5 code, .rendered-markdown h6 tt, .rendered-markdown h6 code{font-size:inherit} .rendered-markdown h1{font-size:28px;color:#000} .rendered-markdown h2{font-size:22px;border-bottom:1px solid #ccc;color:#000} .rendered-markdown h3{font-size:18px} .rendered-markdown h4{font-size:16px} .rendered-markdown h5{font-size:14px} .rendered-markdown h6{color:#777;font-size:14px} .rendered-markdown p, .rendered-markdown blockquote, .rendered-markdown ul, .rendered-markdown ol, .rendered-markdown dl, .rendered-markdown table, .rendered-markdown pre{margin:15px 0} .rendered-markdown hr{border:0 none;color:#ccc;height:4px;padding:0} .rendered-markdown>h2:first-child, .rendered-markdown>h1:first-child, .rendered-markdown>h1:first-child+h2, .rendered-markdown>h3:first-child, .rendered-markdown>h4:first-child, .rendered-markdown>h5:first-child, .rendered-markdown>h6:first-child{margin-top:0;padding-top:0} .rendered-markdown a:first-child h1, .rendered-markdown a:first-child h2, .rendered-markdown a:first-child h3, .rendered-markdown a:first-child h4, .rendered-markdown a:first-child h5, .rendered-markdown a:first-child h6{margin-top:0;padding-top:0} .rendered-markdown h1+p, .rendered-markdown h2+p, .rendered-markdown h3+p, .rendered-markdown h4+p, .rendered-markdown h5+p, .rendered-markdown h6+p{margin-top:0} .rendered-markdown ul, .rendered-markdown ol{padding-left:30px} .rendered-markdown ul li>:first-child, .rendered-markdown ul li ul:first-of-type, .rendered-markdown ol li>:first-child, .rendered-markdown ol li ul:first-of-type{margin-top:0} .rendered-markdown ul ul, .rendered-markdown ul ol, .rendered-markdown ol ol, .rendered-markdown ol ul{margin-bottom:0} .rendered-markdown dl{padding:0} .rendered-markdown dl dt{font-size:14px;font-weight:bold;font-style:italic;padding:0;margin:15px 0 5px} .rendered-markdown dl dt:first-child{padding:0} .rendered-markdown dl dt>:first-child{margin-top:0} .rendered-markdown dl dt>:last-child{margin-bottom:0} .rendered-markdown dl dd{margin:0 0 15px;padding:0 15px} .rendered-markdown dl dd>:first-child{margin-top:0} .rendered-markdown dl dd>:last-child{margin-bottom:0} .rendered-markdown blockquote{border-left:4px solid #DDD;padding:0 15px;color:#777} .rendered-markdown blockquote>:first-child{margin-top:0} .rendered-markdown blockquote>:last-child{margin-bottom:0} .rendered-markdown table th{font-weight:bold} .rendered-markdown table th, .rendered-markdown table td{border:1px solid #ccc;padding:6px 13px} .rendered-markdown table tr{border-top:1px solid #ccc;background-color:#fff} .rendered-markdown table tr:nth-child(2n){background-color:#f8f8f8} .rendered-markdown img{max-width:100%;-moz-box-sizing:border-box;box-sizing:border-box} .rendered-markdown code, .rendered-markdown tt{margin:0 2px;padding:0 5px;border:1px solid #eaeaea;background-color:#f8f8f8;border-radius:3px} .rendered-markdown code{white-space:nowrap} .rendered-markdown pre>code{margin:0;padding:0;white-space:pre;border:0;background:transparent} .rendered-markdown .highlight pre, .rendered-markdown pre{background-color:#f8f8f8;border:1px solid #ccc;font-size:13px;line-height:19px;overflow:auto;padding:6px 10px;border-radius:3px} .rendered-markdown pre code, .rendered-markdown pre tt{margin:0;padding:0;background-color:transparent;border:0}</style>
<div class="rendered-markdown"><h1>Programming Assignment 1</h1>
<p><strong>Fundamentals of Modern Software</strong>
<br  /><strong>Fall 2019</strong>
<br  /><strong>Due 11:59 PM, Wednesday September 11</strong></p>
<p><em>This is your first real programming assignment. It will ensure that you are familiar with basic types, variables, and conditionals, and give you practice specifying and testing precise behavior from a program.</em></p>
<p><strong>REMINDERS</strong></p>
<ol>
<li><strong>When you are done, be sure to submit your work.</strong></li>
<li><strong>You must adhere to the collaboration policy in the syllabus. You MAY NOT copy the code of someone else in the class or allow someone else to copy your code.</strong></li>
<li><strong>Be sure to test your program thoroughly on a wide range of inputs. We will.</strong></li>
<li><strong>Your program's output should match the output in the samples EXACTLY, to the letter. We will grade your work in part using automated tests, and as you have seen, even a single-character difference can cause a comparison not to match.</strong></li>
</ol>
<h2>tax.py</h2>
<p><em>This problem is based on an example from the Georgetown Computer Programming for Lawyers course.</em></p>
<p>Write a program that asks a user to enter their taxable income for 2018 and prints the amount of federal income tax they owe.</p>
<ul>
<li>The tax brackets and rates are listed at
<br  /><a href="https://turbotax.intuit.com/tax-tips/irs-tax-return/current-federal-tax-rate-schedules/L7Bjs1EAD">https://turbotax.intuit.com/tax-tips/irs-tax-return/current-federal-tax-rate-schedules/L7Bjs1EAD</a></li>
<li>Assume that the user is filing as a single individual</li>
<li>The IRS <a href="https://www.irs.gov/instructions/i1042s/ch02.html">requires</a> that all figures be rounded off to the nearest dollar: &ldquo;To round off amounts to the nearest whole dollar, drop amounts under 50 cents and increase amounts from 50 to 99 cents to the next dollar. For example, $1.39 becomes $1 and $2.50 becomes $3.&rdquo;</li>
<li>Assume that the user enters the taxable income as a positive integer (without a dollar sign). You do not need to perform any validation or error-checking on the user's input.</li>
</ul>
<p>Here is a sample transcript of a correctly working program. (Ignore the color highlighting; this is a Codio artifact.)</p>
<pre><code>$ python tax.py
Enter your income in 2018: 1000
You owe $100 in federal income tax
$ python tax.py 
Enter your income in 2018: 10000
You owe $1010 in federal income tax
$ python tax.py
Enter your income in 2018: 100000
You owe $18290 in federal income tax
</code></pre>
<p>Here is some advice: This is a bigger problem than you have dealt with so far. Take it in stages.</p>
<ul>
<li>Write a program that prints out that the user owes $100 in taxes.</li>
<li>Modify the program so that it asks the user to input their income &ndash; and then prints out that they owe $100 in taxes.</li>
<li>Modify the program so that assumes the user's income is in the lowest (10%) bracket and computes the tax owe accordingly.</li>
<li>Modify the program to add the second (12%) bracket: first decide whether the income falls in the 10% or 15% bracket, and then compute the tax owed accordingly.</li>
<li>Repeat with the remaining brackets.</li>
<li>Finish by doing the rounding correctly. There isn't a simple function you can call that rounds numbers exactly as the IRS expects. The most straightforward approach is to translate the IRS's instructions directly into Python.</li>
</ul>
<p><strong>Edit <code>tax.py</code> so that it computes the tax owed. When you are SURE that you are done, select &ldquo;Mark as Completed&rdquo; from the Education menu to submit your code.</strong></p>
</div>