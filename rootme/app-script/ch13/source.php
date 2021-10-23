<code><span style="color: #000000">
#!/usr/bin/env php
<br /><span style="color: #0000BB">&lt;?php<br />
<br />error_reporting</span>
<span style="color: #007700">
   (</span>
        <span style="color: #0000BB">0</span>
        <span style="color: #007700">);
    <br />
</span>
<span style="color: #0000BB">ini_set</span>
<span style="color: #007700">
    (</span>
        <span style="color: #DD0000">"display_errors"</span>
        <span style="color: #007700">, </span>
        <span style="color: #0000BB">0</span>
        <span style="color: #007700">);
    <br /><br />class </span>
<span style="color: #0000BB">Jail<br /></span>
<span style="color: #007700">
    {<br /><br />    function </span>
    <span style="color: #0000BB">filter</span>
    <span style="color: #007700">
        (</span>
        <span style="color: #0000BB">$var</span>
        <span style="color: #007700">)
        {<br />
            if(</span>
                <span style="color: #0000BB">preg_match</span>
                <span style="color: #007700">
                (</span>
                    <span style="color: #DD0000">'/(\'|\"|`|\.|\$|\/|require|include|exec|passthru|shell_exec|system|proc_open|popen|curl_exec|curl_multi_exec|require|require_once|include|include_once|eval|pcntl_exec|file|create_function|asser|extract|fopen|bzopen|gzopen|construct|chgrp|chmod|chown|copy|lchgrp|lchown|link|rmdir|tempnam|touch|dir|stat|read|hash|md5|sha1|hex|bin|highlight|substr|add|chr|convert|join|ord|trim|spaces|die|exit|call_user_func|reflection|break)/i'</span>
                    <span style="color: #007700">, </span>
                    <span style="color: #0000BB">$var</span>
                    <span style="color: #007700">))
        {<br />                return </span>
            <span style="color: #0000BB">false</span>
            <span style="color: #007700">;<br />        }
        <br />        return </span>
        <span style="color: #0000BB">true</span>
        <span style="color: #007700">;
        <br />    }
    <br /><br />    public function </span>
    <span style="color: #0000BB">run</span>
    <span style="color: #007700">()
    {<br />        echo </span>
        <span style="color: #DD0000">"                 _                                          \n"</span>
        <span style="color: #007700">;<br />        echo </span>
        <span style="color: #DD0000">" _ __ ___   ___ | |_       _ __ ___   ___    ___  _ __ __ _ \n"</span>
        <span style="color: #007700">;<br />        echo </span>
        <span style="color: #DD0000">"| '__/ _ \ / _ \| __| ___ | '_ ` _ \ / _ \  / _ \| '__/ _` |\n"</span>
        <span style="color: #007700">;<br />        echo </span>
        <span style="color: #DD0000">"| | | (_) | (_) | |__|___|| | | | | |  __/_| (_) | | | (_| |\n"</span>
        <span style="color: #007700">;<br />        echo </span>
        <span style="color: #DD0000">"|_|  \___/ \___/ \__|     |_| |_| |_|\___(_)\___/|_|  \__, |\n"</span>
        <span style="color: #007700">;<br />        echo </span>
        <span style="color: #DD0000">"                                                      |___/ \n"</span>
        <span style="color: #007700">;<br />        echo </span>
        <span style="color: #DD0000">"You are in jail ! MOUAHAH !                                 \n"</span>
        <span style="color: #007700">;<br />        echo </span>
        <span style="color: #DD0000">"Don't try to escape this one, just go deeper in it.        \n"</span>
        <span style="color: #007700">;<br />        echo </span>
        <span style="color: #DD0000">"Flag is in a subdirectory... Good Luck ! =)                 \n"</span>
        <span style="color: #007700">;<br />
            while(</span>
                <span style="color: #0000BB">true</span>
                <span style="color: #007700">)
                {<br />            echo </span>
                    <span style="color: #DD0000">"&gt;&gt;&gt; "</span>
                    <span style="color: #007700">;<br />            </span>
                    <span style="color: #0000BB">$handle </span>
                    <span style="color: #007700">= </span>
                    <span style="color: #0000BB">fopen </span>
                    <span style="color: #007700">
                        (</span>
                            <span style="color: #DD0000">"php://stdin"</span>
                            <span style="color: #007700">,</span>
                            <span style="color: #DD0000">"r"</span>
                            <span style="color: #007700">);<br />            </span>
                            <span style="color: #0000BB">$cmd </span>
                            <span style="color: #007700">= </span>
                            <span style="color: #0000BB">fgets</span>
                            <span style="color: #007700">
                            (</span>
                                <span style="color: #0000BB">$handle</span>
                                <span style="color: #007700">);<br />
                                if(</span>
                                    <span style="color: #0000BB">$cmd </span>
                                    <span style="color: #007700">!= </span>
                                    <span style="color: #DD0000">"\n"</span>
                                    <span style="color: #007700">)
                                    {<br />
                                        if(</span>
                                            <span style="color: #0000BB">$this</span>
                                            <span style="color: #007700">-&gt;</span>
                                            <span style="color: #0000BB">filter</span>
                                            <span style="color: #007700">
                                            (</span>
                                                <span style="color: #0000BB">$cmd</span>
                                                <span style="color: #007700">))
                                            {<br />                    try {<br />                        </span>
                                            <span style="color: #0000BB">$cmd </span>
                                            <span style="color: #007700">= </span>
                                            <span style="color: #0000BB">substr</span>
                                            <span style="color: #007700">
                                            (</span>
                                                <span style="color: #0000BB">$cmd</span>
                                                <span style="color: #007700">, </span>
                                                <span style="color: #0000BB">0</span>
                                                <span style="color: #007700">, -</span>
                                                <span style="color: #0000BB">1</span>
                                                <span style="color: #007700">);<br />                        </span>
                                                <span style="color: #0000BB">$cmd </span>
                                                <span style="color: #007700">= </span>
                                                <span style="color: #0000BB">str_replace</span>
                                                <span style="color: #007700">
                                                    (</span>
                                                     <span style="color: #DD0000">'__FILE__'</span>
                                                     <span style="color: #007700">,</span>
                                                     <span style="color: #DD0000">"preg_replace('@\(.*\(.*$@', '', __FILE__,1)"</span>
                                                     <span style="color: #007700">,</span>
                                                     <span style="color: #0000BB">$cmd</span>
                                                     <span style="color: #007700">);<br />
                                                        echo eval(</span>
                                                            <span style="color: #0000BB">$cmd</span>
                                                            <span style="color: #007700">.</span>
                                                            <span style="color: #DD0000">';'</span>
                                                            <span style="color: #007700">).</span>
                                                        <span style="color: #DD0000">"\n"</span>
                                                        <span style="color: #007700">;<br />
                                            } catch (</span>
                                            <span style="color: #0000BB">Throwable $e</span>
                                            <span style="color: #007700">)
                                            {<br />                        echo </span>
                                            <span style="color: #DD0000">"\n"</span>
                                            <span style="color: #007700">;<br />                    }<br />
                            }<br />                else{<br />                    echo </span><span style="color: #DD0000">"NOPE!\n"</span><span style="color: #007700">;<br />                }<br />            }<br />            else{<br />                break;<br />            }<br />        }<br />    }<br />}<br /><br />(new </span><span style="color: #0000BB">Jail</span><span style="color: #007700">)-&gt;</span><span style="color: #0000BB">run</span><span style="color: #007700">();<br /><br /></span><span style="color: #0000BB">?&gt;<br /></span>
</span>
</code>
