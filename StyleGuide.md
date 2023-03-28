# Style Guide

## Text
### Heading Levels
    # Heading 1
    ## Heading 2
    ### Heading 3
    ### Heading 4

plain text

    plain text

*italic text*

    *italic text*

**bold text**

    **bold text**

***bold italic text***

    ***bold italic text***

### Code
```python
s = "Python code block"
print(s)
```

    ```python
    s = "Python code block"
    print(s)
    ```

```javascript
var s = "JavaScript code block";
alert(s);
```

    ```javascript
    var s = "JavaScript code block";
    alert(s);
    ```

```html
HTML syntax highlighting. 
But let's throw in another <b>tag</b>.
```

    ```html
    HTML syntax highlighting. 
    But let's throw in another <b>tag</b>.
    ```

```
No language indicated, so no syntax highlighting. 
But let's throw in a <b>tag</b>.
```

    ```
    No language indicated, so no syntax highlighting. 
    But let's throw in a <b>tag</b>.
    ```

## Information Display

### Lists
**Unordered List**
*   item
*   item
    *   sub-item
*   item

**Ordered List**
1.   item
2.   item
3.   item


### Tables

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

| One    | Two | Three | Four    | Five  | Six
|-|-|-|-|-|-
| Span <td colspan=3>triple  <td colspan=2>double

## Images

### Linked Videos

**Traditional HTML**

<a href="http://www.youtube.com/watch?feature=player_embedded&v=eJojC3lSkwg" target="_blank"><img src="http://img.youtube.com/vi/eJojC3lSkwg/0.jpg" alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

    <a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VID_ID_HERE" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VID_ID_HERE/0.jpg" alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

**Pure Markdown**

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/eJojC3lSkwg/0.jpg)](http://www.youtube.com/watch?v=eJojC3lSkwg)

    [![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/YOUTUBE_VID_ID_HERE/0.jpg)](http://www.youtube.com/watch?v=YOUTUBE_VID_ID_HERE)


```plantuml
@startuml
    skinparam backgroundColor #EEEBDC
    skinparam handwritten true
    actor Customer
    Customer -> "login()" : username & password
    "login()" -> Customer : session token
    activate "login()"
    Customer -> "placeOrder()" : session token, order info
    "placeOrder()" -> Customer : ok
    Customer -> "logout()"
    "logout()" -> Customer : ok
    deactivate "login()"
@enduml
```

### Flowchart

```mermaid
graph LR
A[Hard edge] -->B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```


### Gantt Chart

```mermaid
%% Example with selection of syntaxes
        gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid

        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2               :         des4, after des3, 5d

        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d

        section Documentation
        Describe gantt syntax               :active, a1, after des1, 3d
        Add gantt diagram to demo page      :after a1  , 20h
        Add another diagram to demo page    :doc1, after a1  , 48h

        section Last section
        Describe gantt syntax               :after doc1, 3d
        Add gantt diagram to demo page      : 20h
        Add another diagram to demo page    : 48h
```


### Class Diagram

```mermaid
classDiagram
      Animal <|-- Duck
      Animal <|-- Fish
      Animal <|-- Zebra
      Animal : +int age
      Animal : +String gender
      Animal: +isMammal()
      Animal: +mate()
      class Duck{
          +String beakColor
          +swim()
          +quack()
      }
      class Fish{
          -int sizeInFeet
          -canEat()
      }
      class Zebra{
          +bool is_wild
          +run()
      }
```

### State Diagram

```mermaid
stateDiagram
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```

### Pie Chart

```mermaid
pie
    title Pie Chart
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 150 
```










Resources:
https://support.typora.io/Draw-Diagrams-With-Markdown/
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet