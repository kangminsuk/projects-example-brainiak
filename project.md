---
---
## What are Projects?

```yaml
type: NotebookTask
```

`@context`

In this project, we will analyze a fascinating dataset on every single lego block that has ever been built!

![lego](https://sh-s7-live-s.legocdn.com/is/image/LEGOMKTG/pick-a-brick--201606--gl--banner-background--small)

`@instructions`

As a datacamp user, you have been working hard, learning the fundamentals of data science, by doing many [courses]() we offer, and practicing these skills by taking our [challenges](). 
Our vision behind __Projects__ is to take this many steps forward, and  allow you apply these skills to carry out an __end-to-end analysis__, on a __real-world task__, using __real-world__ tools and workflows, and be able to __showcase__ your work. In this __Introduction to Projects__, you will learn how projects work, and familiarize yourself with the new interface.

For your first task: 

- Read the first paragraph on the right to familiarize yourself with the narrative for you project! 
- Feel free to poke around the interface. 
- When you are finished, click on the __Next Task__ button at the bottom.  

`@hint`

You don't really need a hint for this task!

`@sample_code`

```{python}
# Nothing to do here
```

`@solution`

```{python}
# Nothing to do here!
```

`@tests`

```{python}
%%nose
def test_default():
  assert True
```

---

## The Projects Interface

```yaml
type: NotebookTask
```

`@context`

This comprehensive database of lego blocks is provided by [Rebrickable](https://rebrickable.com/downloads/). The data is available as csv files and the schema is shown below.

![schema](https://s.rebrickable.com/static/img/diagrams/downloads_schema.png)

Let us start by reading in the colors data to get a sense of the diversity of lego sets!

`@instructions`

The project interface consists of a __jupyter notebook__ on the right and an __instructional sidebar__ on the left.

1. The  [Jupyter Notebook](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) contains the main narrative for the project. It contains the story you will be working on, supported by all the code you write, and the output tables and plots, that you will create.

2. The __instructional sidebar__ contains `instructions`, `hints`, and other pedagogical elements that will aid you in you in your quest to complete your project successfully and come up with a newsworthy story! This portion of the interface works almost the same way as courses.

For your second task:

- Shift your attention to the content on top of the notebook. 
- Read it to understand the narrative. 
- Click on the box/cell containing code, press `Ctrl + Enter`, and notice what happens!
- When you are finished, click on the __Next Task__ button at the bottom.

`@hint`

Navigate to the cell containing code and press `Shift + Enter` to execute it.

`@sample_code`

```{python}
# Import modules
import pandas as pd

# Read colors data
colors = pd.read_csv('/usr/local/share/datasets/colors.csv')

# Print the first few rows
colors.head()
```

`@solution`

```{python}
# Import modules
import pandas as pd

# Read colors data
colors = pd.read_csv('/usr/local/share/datasets/colors.csv')

# Print the first few rows
colors.head()
```

`@tests`

```{python}
%%nose
def test_colors_exists():
    assert 'colors' in globals(), "You should read the data into a variable named `colors`"
```

---

## Welcome to Jupyter!

```yaml
type: NotebookTask
```

`@context`

Now that we have read the `colors` data, we can start exploring it! Let us start by understanding the number of colors available.

`@instructions`

If this is your first brush with [Jupyter Notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html), continue reading this. Otherwise, go and dig into the notebook directly to explore lego blocks, and build your narrative! For those of you who choose to leave us here, don't worry, we will meet you again at the end of this journey.

As you might have already noticed, doing data science in the real world is all about building an interesting story around your data. As a result, your narrative around the data is as important as the code you write, and the outputs you generate. Jupyter Notebooks provide an awesome environment that allows you to do precisely this by combining text, code and outputs into one single document.

![jupyter-notebook](https://www.dataquest.io/blog/images/jupyter/interface-screenshot.png)


In this task, you will 

- Create a variable named `num_colors` that counts the number of distinct colors.
- Print it out.

`@hint`

You can inspect the dimensions of `colors` using `colors.shape`.

`@sample_code`

```{python}
# How many distinct colors are available?
# -- YOUR CODE HERE --
```

`@solution`

```{python}
# How many distinct colors are available?
num_colors = colors.rgb.size
print("Number of distinct colors:", num_colors)
```

`@tests`

```{python}
%%nose
def test_num_colors():
    assert num_colors == 135, "The variable num_colors should equal 135"
```

---

## Using the Notebook

```yaml
type: NotebookTask
```

`@context`

The `colors` data has a column named `is_trans` that indicates whether a color is transparent or not. It would be interesting to explore the distribution of transparent vs. non-transparent colors.

`@instructions`

A Jupyter Notebook consists of cells, each of which can contain code or markdown text. Jupyter Notebooks support code in multiple languages (like R, Python, Julia etc.), using a system of kernels. This notebook connects to a Python 3 kernel, and hence allows us to write Python code!  In this task, we will explore how to add a new cell to the notebook, write some python code to support the narrative, and execute it. Are you ready?

A picture is worth a thousand words. So instead of describing how to work with cells in a notebook, here is an interactive gif to walk you through the steps.

![Working with Cells](http://media.giphy.com/media/l378dk9Vx9JWj47ug/giphy.gif)

You can read more about notebooks in this [comprehensive tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook).

<hr/>

In this task, you will:

- Summarize colors based on their transparency.
- Save it as a variable named `colors_summary`.
- Print out `colors_summary`

Executing your code should result in the table shown below.

![colors_summary](https://imgur.com/OtvmT9E.png)

Additionally,

- Insert a new cell by clicking on `Cell > Insert Cell Below`
- Change its type to `markdown` using the toolbar on the top of the notebook.
- Enter some text (in markdown) to share something interesting about the output table above it.

After you are completed this task, feel free to play around adding new cells, editing them, modifying their type, executing code, etc. Explore as much as you want to, and when you are ready click on `Next Task` to move on to the next task.

`@hint`

Shown below is some code to help you complete this task!

```python
# Summarize colors based on whether they are transparent or not?
colors_summary = colors.___(___).count()
colors_summary
```

`@sample_code`

```{python}
# colors_summary: Distribution of colors based on transparency
# -- YOUR CODE HERE --
```

`@solution`

```{python}
# Summarize colors based on whether they are transparent or not?
colors_summary = colors.groupby("is_trans").count()
colors_summary
```

`@tests`

```{python}
%%nose
def test_colors_summary_exists():
    assert 'colors_summary' in globals(), "You should have defined a variable named `colors_summary`"
def test_colors_summary():
    assert colors_summary.shape == (2, 3), "The DataFrame colors_summary should contain 2 rows and 3 columns"
```

---

## Working on Tasks

```yaml
type: NotebookTask
```

`@context`

Another interesting dataset available in this database is the `sets` data. It contains a comprehensive list of sets over the years and the number of parts that each of these sets contained. 

![sets_data](https://imgur.com/1k4PoXs.png)

Let us use this data to explore how the average number of parts in lego sets has varied over the years.

`@instructions`

Every project is broken down into a number of smaller tasks. In order to complete a task, you will need to:
    
1. Read the narrative in the notebook to understand the scope of the task.
2. Read the instructions in the sidebar to get more details on what is expected.
3. Write code in the notebook and run it by by pressing `Ctrl + Enter`, or clicking on the Run icon in the toolbar. 

Let us follow these steps to complete this task.


In this task, you will:


- Read the data in `/usr/local/share/datasets/sets.csv` as a `DataFrame` named `sets`
- Create a summary of the average parts per year and save it as `parts_per_year`
- Plot the average number of parts per year.

The first few rows of `parts_per_year` should resemble the table shown below:

![parts-per-year](https://imgur.com/P0x36gr.png)



`@hint`

Shown below is some code to help you complete this task!

```python
sets = pd.___(___)
parts_by_year = sets[['year', 'num_parts']].\
  ___(___, as_index = False).\
  ___()
parts_by_year.plot(x = ___, y = ___)
```

`@sample_code`

```{python}
%matplotlib inline
# Read sets data as `sets`

# Create a summary of average number of parts by year: `parts_by_year`

# Plot trends in average number of parts by year


```

`@solution`

```{python}
%matplotlib inline
sets = pd.read_csv('/usr/local/share/datasets/sets.csv')
parts_by_year = sets[['year', 'num_parts']].\
  groupby('year', as_index = False).\
  mean()
parts_by_year.head()
parts_by_year.plot(x = 'year', y = 'num_parts')
sets.head()
```

`@tests`

```{python}
%%nose
def test_sets_exists():
    assert 'sets' in globals(), "You should read the data into a variable named `sets`"
def test_parts_by_year_exists():
    assert 'parts_by_year' in globals(), "You should have defined a variable named `parts_by_year`"
```

---

## Checking your Work

```yaml
type: NotebookTask
```

`@context`

Lego blocks ship under multiple themes. Let us try and get a sense of how the number of themes shipped has varied over the years.

`@instructions`

At any point in the project, you can click on the __Check Project__ button at the bottom to test whether your output matches the solution.

- If all the tests pass, your task circle will turn green. 
- If some tests fail, your task circle with turn orange. 

You can view the test results in the sidebar to understand what failed and update your code accordingly. If you are unable to get all the tests to pass despite repeated attempts, you can click on the __Hint__ button to get a useful hint.

---

In this task

- Create a summary of the number of themes shipped by year.
- Save it as a `DataFrame` named `themes_by_year`.

The first few rows of your data should resemble the table shown below.

![themes_by_year](https://imgur.com/SC9UXEf.png)

`@hint`

Shown below is some code to help you complete this task:

```python
themes_by_year = sets[[___, ___]].\
  ___(___, as_index = False).\
  ___()
themes_by_year.___()
```

`@sample_code`

```{python}
# themes_by_year: Number of themes shipped by year
# -- YOUR CODE HERE --
```

`@solution`

```{python}
# themes_by_year: Number of themes shipped by year
themes_by_year = sets[['year', 'theme_id']].\
  groupby('year', as_index = False).\
  count()
themes_by_year.head()
```

`@tests`

```{python}
%%nose
def test_themes_by_year_exists():
    assert 'themes_by_year' in globals(), "You should have defined a variable named `themes_by_year`"
def test_themes_by_year():
    assert themes_by_year.shape == (66, 2), "The DataFrame themes_by_year should contain 66 rows and 2 columns"
def test_themes_by_year_names():
    colnames = ['year', 'theme_id']
    assert all(name in themes_by_year for name in colnames), "Your DataFrame, bnames, should have columns named: year, theme_id"
```

---

## Next Steps

```yaml
type: NotebookTask
```

`@context`

Lego blocks offer an unlimited amoung of fun across ages. We explored some interesting trends around colors, parts and themes. 

`@instructions`

Congratulations on completing your tasks successfully! How did it feel seeing the circle go green? Pretty awesome right?

![success](https://media.giphy.com/media/a0h7sAqON67nO/giphy.gif)

You are now ready to get started with your first project. Read this [comprehensive guide](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook) to learn more about how to work with Jupyter Notebooks.

`@hint`

You don't need help with this one!

`@sample_code`

```{python}
# Nothing to do here
```

`@solution`

```{python}
# Nothing to do here
```

`@tests`

```{python}
%%nose
def test_default():
  assert True
```
