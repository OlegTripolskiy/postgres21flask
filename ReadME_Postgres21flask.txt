1. ���� ������ ����� 09.06.2021
2. ������ �������� ������ ������� � D:\OPENSERVER\OSPanel\domains\postgres2021

3. �������: ������� �� ��������� FLASK:
   ���������� ���� � ������ �� ����� ��� ���:
      - ����������� ����� ����� ��������� � ����� static.
      - ���������  ���� ����� ���������� � ����� templates.
   ��������:
   �������� ��� ����� ������� �� index.html
   �������� ���� � ����������� ������:
      a) � ����� ����� �:
         <!--  ���� � ������ ���� �� ������� Flask -->
           <link rel="stylesheet" type="text/css" href="static/css/main.css" /> 
           <link id="link_chcolor" rel="stylesheet" type="text/css" href="static/css/color_grey.css" /> 
           <link rel="icon" href="static/favicon.ico">

           <!--  ����������� ���������� Highligt.JS  -->
         <!--  ���� � ������ ���� �� ������� Flask -->
           <link rel="stylesheet" href="static/css/higligt_gml.css">
           <link rel="preload" href="static/static/js/highlight.pack.js" as="script">
           <script src="static/js/highlight.pack.js"></script>

      b) � ������� ������� ����� static � ����/ 
         // ==== ����� ������ ����� ===============
          $(".color_scheme tr td").click(function () {
             ...
             let colorFileNname = "static/css/" + idAttr + ".css"; // ������� ���� � ����� ������ ������.
      c

4. 
5. �����
