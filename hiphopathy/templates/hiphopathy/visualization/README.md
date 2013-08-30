research
========

for my research files relating to the HipHopathy research project

this holds:
  
  - demo html page to show how the line graph can be used
  - css stylesheet for the line graph
  - javascript file for the line graph
  - JSON example file to show how a JSON file should be formatted for the line graph

if you would like to see an example in action with random data, go to
http://alex.heartdrops.org/researchgraph01.html


<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>Jay-Z Song Graph: User vs Jay-Z</title>
		<script type="text/javascript" src="d3.v2.js"></script>
		<link href="lineGraphStyle.css" rel="stylesheet" type="text/css" />
	</head>

		-------------------------------------------------- */

              /* Base class */
          .bs-docs-example {
              position: relative;
              margin: 15px 0;
              padding: 39px 19px 14px;
              *padding-top: 19px;
              background-color: #fff;
              border: 1px solid #ddd;
              -webkit-border-radius: 4px;
              -moz-border-radius: 4px;
              border-radius: 4px;
          }

              /* Echo out a label for the example */
          .bs-docs-example:after {
              content: "Example";
              position: absolute;
              top: -1px;
              left: -1px;
              padding: 3px 7px;
              font-size: 12px;
              font-weight: bold;
              background-color: #f5f5f5;
              border: 1px solid #6d697a;
              color: #9da0a4;
              -webkit-border-radius: 4px 0 4px 0;
              -moz-border-radius: 4px 0 4px 0;
              border-radius: 4px 0 4px 0;
          }

          .bs-docs-definition {
              position: relative;
              margin: 15px 0;
              padding: 39px 19px 14px;
              *padding-top: 19px;
              background-color: #fff;
              border: 1px solid #ddd;
              -webkit-border-radius: 4px;
              -moz-border-radius: 4px;
              border-radius: 4px;
          }

              /* Echo out a label for the example */
          .bs-docs-definition:after {
              content: "";
              position: absolute;
              top: -1px;
              left: -1px;
              padding: 3px 7px;
              font-size: 12px;
              font-weight: bold;
              background-color: #a9dba9;
              border: 1px solid #ddd;
              color: #9da0a4;
              -webkit-border-radius: 4px 0 4px 0;
              -moz-border-radius: 4px 0 4px 0;
              border-radius: 4px 0 4px 0;
          }
              /* Remove spacing between an example and it's code */
          .bs-docs-example + .prettyprint {
              margin-top: -20px;
              padding-top: 15px;
          }

              /* Tweak examples
              ------------------------- */
          .bs-docs-example > p:last-child {
              margin-bottom: 0;
          }
          .bs-docs-example .table,
          .bs-docs-example .progress,
          .bs-docs-example .well,
          .bs-docs-example .alert,
          .bs-docs-example .hero-unit,
          .bs-docs-example .pagination,
          .bs-docs-example .navbar,
          .bs-docs-example > .nav,
          .bs-docs-example blockquote {
              margin-bottom: 5px;
          }
          .bs-docs-example .pagination {
              margin-top: 0;
          }
          .bs-navbar-top-example,
          .bs-navbar-bottom-example {
              z-index: 1;
              padding: 0;
              height: 90px;
              overflow: hidden; /* cut the drop shadows off */
          }
          .bs-navbar-top-example .navbar-fixed-top,
          .bs-navbar-bottom-example .navbar-fixed-bottom {
              margin-left: 0;
              margin-right: 0;
          }
          .bs-navbar-top-example {
              -webkit-border-radius: 0 0 4px 4px;
              -moz-border-radius: 0 0 4px 4px;
              border-radius: 0 0 4px 4px;
          }
          .bs-navbar-top-example:after {
              top: auto;
              bottom: -1px;
              -webkit-border-radius: 0 4px 0 4px;
              -moz-border-radius: 0 4px 0 4px;
              border-radius: 0 4px 0 4px;
          }
          .bs-navbar-bottom-example {
              -webkit-border-radius: 4px 4px 0 0;
              -moz-border-radius: 4px 4px 0 0;
              border-radius: 4px 4px 0 0;
          }
          .bs-navbar-bottom-example .navbar {
              margin-bottom: 0;
          }
          form.bs-docs-example {
              padding-bottom: 19px;
          }
              /* Faded out hr */
          hr.soften {
              height: 1px;
              margin: 70px 0;
              background-image: -webkit-linear-gradient(left, rgba(0,0,0,0), rgba(0,0,0,.1), rgba(0,0,0,0));
              background-image:    -moz-linear-gradient(left, rgba(0,0,0,0), rgba(0,0,0,.1), rgba(0,0,0,0));
              background-image:     -ms-linear-gradient(left, rgba(0,0,0,0), rgba(0,0,0,.1), rgba(0,0,0,0));
              background-image:      -o-linear-gradient(left, rgba(0,0,0,0), rgba(0,0,0,.1), rgba(0,0,0,0));
              border: 0;
          }
          .masthead {

        color: #ff1d40;


          }



 {% extends "base.html" %}

{% block title %}Hiphopathy: Snippets{% endblock %}

{% block navbar %}
<li><a href="/hiphopathy/">Home</a></li>
<li><a href="/hiphopathy/tutorial_1/">How To</a></li>
<li><a href="/hiphopathy/about/">About</a></li>
<li><a href="/hiphopathy/search_form/">Search</a></li>
<li><a href="/hiphopathy/contact/">Contact</a></li>
{% endblock %}

{% block jumbotron %}
<h2>Snippets to decode</h2>

{% endblock %}

{% block marketing %}





<div class="mini-layout fluid">
    <div class="row-fluid">
        <div class="mini-layout-sidebar">
        <!--Sidebar content-->
            <table class="table table-condensed table-striped table-bordered">
            <caption>Decoding Algorithm</caption>
            <tbody>
            <tr>
                <td>1 </td>
                <td>Read the sentence(s) thoroughly</td>
            </tr>
            <tr>
                <td>2 </td><td> Identify metaphors (distinguish between literal and metaphorical language in text).</td>
            </tr>
            <tr>
                <td>2</td> <td>Determine the context</td>
            </tr>
            <tr>
                <td>3</td> <td>Make your first translation</td>
            </tr>
            <tr>
                <td>2</td><td>Use the abstraction process to decide which words to focus on<br>
                In our case, we will use an heuristic to focus our attention. Since one of the goals of
                this project is understanding how we reason about conceptual metaphors, we will use knowledge of conceptual
                metaphor research in natural language understanding to guide our solution<sup>1</sup>. In that field, they follow
                the heuristic of focusing on noun and verb phrases, with particular attention to action verbs.<br>
                <small class="pull-right">[1] E. Shutova. Models of Metaphor in NLP. Computational Linguistics, (July):688–697, 2010.</small>
            </td>
            </tr>
            </tbody>
        </table>
        </div>
        <div class="mini-layout-body">
        <!--Body content-->
            <form class="form-horizontal" method="post" action=".">{% csrf_token %}
            {% for field in form %}
            <div class="control-group">
                <label class="control-label">{{field.label}} :</label>
                <div class="controls">
                  {{field}}
                </div><br>
            </div>
            {% endfor %}
            <br>
            </form> <!-- {{ form.as_p }}   -->
            <div class="control-group">
                <div class="controls">
                  <button type="submit" class="btn">Submit</button>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}



SLYVIE
{'decoded': u'sad', 'snippetid': 1L, 'chunk': u'This is the shit you dream about with the homies steaming out',
'comments': u'This line has not being decoded by Jay',
'user_answer': u'dream', 'songid_id': 185L},

{'decoded': u'beginnings, dreaming, dangerous, good/bad', 'snippetid': 2L, 'chunk': u'Back, back, backing them Beemers out',
'comments': u'beginnings, dreaming, holla', 'user_answer': u'luxury, cars, ride', 'songid_id': 185L},

{'decoded': u'albert', 'snippetid': 3L, 'chunk': u"Seems as our plans to get a grant\r\nThen go off to college, didn't pan or even out",
'comments': u'Not decoded', 'user_answer': u'plan', 'songid_id': 185L},

{'decoded': u'not', 'snippetid': 4L, 'chunk': u'We need it now, we need a town',
'comments': u'not', 'user_answer': u'baseball', 'songid_id': 185L}
