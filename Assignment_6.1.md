
Read the dataset from the below link


```python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
```


```python
df=pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Unnamed: 0</th>
      <th>Id</th>
      <th>Name</th>
      <th>Year</th>
      <th>Gender</th>
      <th>State</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11349</td>
      <td>11350</td>
      <td>Emma</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>62</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11350</td>
      <td>11351</td>
      <td>Madison</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>48</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11351</td>
      <td>11352</td>
      <td>Hannah</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11352</td>
      <td>11353</td>
      <td>Grace</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11353</td>
      <td>11354</td>
      <td>Emily</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>41</td>
    </tr>
  </tbody>
</table>
</div>



1. Delete unnamed columns


```python
df.drop(df.columns[df.columns.str.contains('unnamed',case = False)],axis = 1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Id</th>
      <th>Name</th>
      <th>Year</th>
      <th>Gender</th>
      <th>State</th>
      <th>Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11350</td>
      <td>Emma</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>62</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11351</td>
      <td>Madison</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>48</td>
    </tr>
    <tr>
      <th>2</th>
      <td>11352</td>
      <td>Hannah</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>46</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11353</td>
      <td>Grace</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>44</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11354</td>
      <td>Emily</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>41</td>
    </tr>
    <tr>
      <th>5</th>
      <td>11355</td>
      <td>Abigail</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>37</td>
    </tr>
    <tr>
      <th>6</th>
      <td>11356</td>
      <td>Olivia</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>33</td>
    </tr>
    <tr>
      <th>7</th>
      <td>11357</td>
      <td>Isabella</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>30</td>
    </tr>
    <tr>
      <th>8</th>
      <td>11358</td>
      <td>Alyssa</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>29</td>
    </tr>
    <tr>
      <th>9</th>
      <td>11359</td>
      <td>Sophia</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>28</td>
    </tr>
    <tr>
      <th>10</th>
      <td>11360</td>
      <td>Alexis</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>27</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11361</td>
      <td>Elizabeth</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>27</td>
    </tr>
    <tr>
      <th>12</th>
      <td>11362</td>
      <td>Hailey</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>27</td>
    </tr>
    <tr>
      <th>13</th>
      <td>11363</td>
      <td>Anna</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>26</td>
    </tr>
    <tr>
      <th>14</th>
      <td>11364</td>
      <td>Natalie</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>25</td>
    </tr>
    <tr>
      <th>15</th>
      <td>11365</td>
      <td>Sarah</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>25</td>
    </tr>
    <tr>
      <th>16</th>
      <td>11366</td>
      <td>Sydney</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>25</td>
    </tr>
    <tr>
      <th>17</th>
      <td>11367</td>
      <td>Ava</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>23</td>
    </tr>
    <tr>
      <th>18</th>
      <td>11368</td>
      <td>Trinity</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>22</td>
    </tr>
    <tr>
      <th>19</th>
      <td>11369</td>
      <td>Haley</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>21</td>
    </tr>
    <tr>
      <th>20</th>
      <td>11370</td>
      <td>Kaylee</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>21</td>
    </tr>
    <tr>
      <th>21</th>
      <td>11371</td>
      <td>Taylor</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>21</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11372</td>
      <td>Chloe</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>20</td>
    </tr>
    <tr>
      <th>23</th>
      <td>11373</td>
      <td>Ella</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>20</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11374</td>
      <td>Mackenzie</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>20</td>
    </tr>
    <tr>
      <th>25</th>
      <td>11375</td>
      <td>Sierra</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>19</td>
    </tr>
    <tr>
      <th>26</th>
      <td>11376</td>
      <td>Kayla</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>18</td>
    </tr>
    <tr>
      <th>27</th>
      <td>11377</td>
      <td>Samantha</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>18</td>
    </tr>
    <tr>
      <th>28</th>
      <td>11378</td>
      <td>Zoe</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>18</td>
    </tr>
    <tr>
      <th>29</th>
      <td>11379</td>
      <td>Jessica</td>
      <td>2004</td>
      <td>F</td>
      <td>AK</td>
      <td>17</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1016365</th>
      <td>5647397</td>
      <td>Brooks</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016366</th>
      <td>5647398</td>
      <td>Calvin</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016367</th>
      <td>5647399</td>
      <td>Cameron</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016368</th>
      <td>5647400</td>
      <td>Dalton</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016369</th>
      <td>5647401</td>
      <td>Dawson</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016370</th>
      <td>5647402</td>
      <td>Edward</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016371</th>
      <td>5647403</td>
      <td>Elias</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016372</th>
      <td>5647404</td>
      <td>Gage</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016373</th>
      <td>5647405</td>
      <td>Hayden</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016374</th>
      <td>5647406</td>
      <td>Jasper</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016375</th>
      <td>5647407</td>
      <td>Jose</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016376</th>
      <td>5647408</td>
      <td>Kaiden</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016377</th>
      <td>5647409</td>
      <td>Kaleb</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016378</th>
      <td>5647410</td>
      <td>Kasen</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016379</th>
      <td>5647411</td>
      <td>Kyson</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016380</th>
      <td>5647412</td>
      <td>Lukas</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016381</th>
      <td>5647413</td>
      <td>Myles</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016382</th>
      <td>5647414</td>
      <td>Nathaniel</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016383</th>
      <td>5647415</td>
      <td>Nolan</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016384</th>
      <td>5647416</td>
      <td>Oakley</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016385</th>
      <td>5647417</td>
      <td>Odin</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016386</th>
      <td>5647418</td>
      <td>Paxton</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016387</th>
      <td>5647419</td>
      <td>Raymond</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016388</th>
      <td>5647420</td>
      <td>Richard</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016389</th>
      <td>5647421</td>
      <td>Rowan</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016390</th>
      <td>5647422</td>
      <td>Seth</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016391</th>
      <td>5647423</td>
      <td>Spencer</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016392</th>
      <td>5647424</td>
      <td>Tyce</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016393</th>
      <td>5647425</td>
      <td>Victor</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1016394</th>
      <td>5647426</td>
      <td>Waylon</td>
      <td>2014</td>
      <td>M</td>
      <td>WY</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
<p>1016395 rows × 6 columns</p>
</div>



2.Show the distribution of male and female


```python
Freq_tab = pd.crosstab(index=df["Gender"],  # Make a crosstab
                              columns="count")      # Name the count column

Freq_tab


```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>col_0</th>
      <th>count</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>F</th>
      <td>558846</td>
    </tr>
    <tr>
      <th>M</th>
      <td>457549</td>
    </tr>
  </tbody>
</table>
</div>



3. Show the top 5 most preferred names


```python
df_top_freq =pd.crosstab(index=df["Name"],  # Make a crosstab
                              columns="count")

df_top_sort=df_top_freq.sort_values(by="count",ascending=False)
df_top_sort.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>col_0</th>
      <th>count</th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Riley</th>
      <td>1112</td>
    </tr>
    <tr>
      <th>Avery</th>
      <td>1080</td>
    </tr>
    <tr>
      <th>Jordan</th>
      <td>1073</td>
    </tr>
    <tr>
      <th>Peyton</th>
      <td>1064</td>
    </tr>
    <tr>
      <th>Hayden</th>
      <td>1049</td>
    </tr>
  </tbody>
</table>
</div>



4.What is the median name occurence in the dataset


```python
5. Distribution of male and female born count by states
```


```python
pd.crosstab(df.Gender, df.State)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>State</th>
      <th>AK</th>
      <th>AL</th>
      <th>AR</th>
      <th>AZ</th>
      <th>CA</th>
      <th>CO</th>
      <th>CT</th>
      <th>DC</th>
      <th>DE</th>
      <th>FL</th>
      <th>...</th>
      <th>SD</th>
      <th>TN</th>
      <th>TX</th>
      <th>UT</th>
      <th>VA</th>
      <th>VT</th>
      <th>WA</th>
      <th>WI</th>
      <th>WV</th>
      <th>WY</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>F</th>
      <td>2404</td>
      <td>9878</td>
      <td>7171</td>
      <td>14518</td>
      <td>45144</td>
      <td>11424</td>
      <td>6575</td>
      <td>3053</td>
      <td>2549</td>
      <td>25781</td>
      <td>...</td>
      <td>2838</td>
      <td>13063</td>
      <td>39760</td>
      <td>9515</td>
      <td>14759</td>
      <td>1398</td>
      <td>13329</td>
      <td>10549</td>
      <td>4305</td>
      <td>1456</td>
    </tr>
    <tr>
      <th>M</th>
      <td>2587</td>
      <td>8419</td>
      <td>6475</td>
      <td>10820</td>
      <td>31637</td>
      <td>9183</td>
      <td>5733</td>
      <td>3000</td>
      <td>2440</td>
      <td>20070</td>
      <td>...</td>
      <td>2908</td>
      <td>10588</td>
      <td>27791</td>
      <td>8233</td>
      <td>11997</td>
      <td>1618</td>
      <td>11049</td>
      <td>8940</td>
      <td>3733</td>
      <td>1904</td>
    </tr>
  </tbody>
</table>
<p>2 rows × 51 columns</p>
</div>




```python

```


```python

```


```python

```


```python

```


```python

```
