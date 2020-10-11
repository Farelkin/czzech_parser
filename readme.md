<h1>Test Task</h1>
<h2>Parser</h2>

<h3>Что нужно сделать?</h3> 
Выгрузить наиболее полные представленные данные по каждому объекту в 
представленном девелоперском проекте недвижимости. 

<h3>Где находится ифнормация по объектам?</h3>
<a href="https://www.italska8.cz/byty">https://www.italska8.cz/byty </a>

<h3>Какую ифнормацию берем?</h3>
<ol>
<li>ID квартиры - ID</li>
<li>Dispozice - Počet pokoju - планировка - floor_plan </li>
<li>Patro / Podlaží – этаж - floor (число)</li>
<li>Plocha – Площадь – area (число) </li>
<li>Stav - доступность - status (на выходе одно из 3 значений available/reserved/sold)</li>
<li>Цена – price (число)</li>
<li>Typ – type</li>
</ol>

<h3>Что ещё?</h3>
<p>Ссылка на объект, пример, <a href="https://www.italska8.cz/bytova-jednotka-01-kopie">https://www.italska8.cz/bytova-jednotka-01-kopie</a></p>
<p>Внутри каждой страницы объекта может находиться дополнительная информация.</p>
<ul>
<li>8 - Размер террасы - terrace (число)</li>
</ul>

<h2>Как запустить готовое задание?</h2>
<ol>
<li>Скачать проект</li>
<li>Выполнить <code>pip install -r requirements.txt</code></li>
<li>Запустить файл main.py</li>
</ol>
<p>Результаты можно посмотреть открыв parser_db.sqlite3</p>
