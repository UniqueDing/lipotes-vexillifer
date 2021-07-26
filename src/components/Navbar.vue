<template>
    
<div class="headercontent fixed-top">
<nav class="navbar navbar-expand-sm navbar-light bg-light headnav">
    <a class="navbar-brand" href="/">Blog</a>
    <button class="navbar-toggler btn-link" style="outline: none;border: none" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item">
                <a class="nav-link" id="index" href="/">{{$t('navbarhome')}}</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="article" href="/article">{{$t('home')}}</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="picture" href="/picture">图片</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" id="about" href="/about">关于</a>
            </li>
        </ul>
        <div class="flex-row navbar-nav">
            <li class="nav-item">
                    <a class="nav-link" id="about" href="?lang=zh">中文</a>
            </li>
			<!-- <li> -->
			<!-- 	<input class="form-control mr-sm-2" type="search" placeholder="{% if lang == 'en' %}SEARCH{% else %}搜索{% endif %}" aria-label="Search"> -->
			<!-- </li> -->
        </div>
        <form class="form-inline my-2 my-lg-0"> 
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search"> 
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button> 
        </form> 
    </div>
</nav>
</div>
</template>

<script>
</script>
