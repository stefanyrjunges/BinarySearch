<h1>Binary Search in a Random Integer Array</h1>

<p>This repository contains a Python script that generates an array of random integers, sorts the array, and then performs a binary search to find a user-specified integer. The script also saves the sorted array to a CSV file for future reference.</p>

<h2>Features</h2>
<ul>
    <li>Generates <strong>100 random integers</strong> between 0 and 1000.</li>
    <li>Sorts the generated integers in ascending order.</li>
    <li>Implements a <strong>binary search algorithm</strong> to find the integer entered by the user.</li>
    <li>Displays how many iterations the binary search took to find the number or informs the user if the number is not found.</li>
    <li>Saves the sorted array to a CSV file called <code>myData.csv</code>.</li>
</ul>

<h2>How It Works</h2>

<ol>
    <li><strong>Random Integer Generation</strong>:
        <ul>
            <li>The script generates 100 random integers between 0 and 1000 using NumPy.</li>
        </ul>
    </li>
    <li><strong>Binary Search</strong>:
        <ul>
            <li>The list of integers is sorted in ascending order.</li>
            <li>The user is prompted to input a number.</li>
            <li>The binary search algorithm is applied to find the user-specified number.</li>
            <li>The number of iterations required to find the number is displayed, or a message is printed if the number is not found.</li>
        </ul>
    </li>
    <li><strong>Saving the Sorted Data</strong>:
        <ul>
            <li>The sorted list of integers is saved as a CSV file (<code>myData.csv</code>), with values separated by commas.</li>
        </ul>
    </li>
</ol>

<h2>Usage</h2>

<ol>
    <li>Clone this repository:
        <pre><code>git clone https://github.com/yourusername/your-repo-name.git</code></pre>
    </li>
    <li>Install the required library:
        <pre><code>pip install numpy</code></pre>
    </li>
    <li>Run the script:
        <pre><code>python DataManag.py</code></pre>
    </li>
    <li>Input the number you'd like to search for when prompted.</li>
</ol>

<h2>Example</h2>

<ol>
    <li>The script will output the sorted array of random integers like this:
        <pre><code>[15 34 55  ... 973]</code></pre>
    </li>
    <li>Enter a number to search for:
        <pre><code>Enter query: 55</code></pre>
    </li>
    <li>The output will either indicate the number of iterations it took to find the number or that the number was not found:
        <pre><code>Data found after 4 iterations</code></pre>
    </li>
    <li>The sorted list is saved as <code>myData.csv</code>.</li>
</ol>
