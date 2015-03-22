<!DOCTYPE html>
<html>
    <head>
        <title>US State and Territory Flags - Resize, reformat and download.</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="United States Flags"/>
        <link rel="shortcut icon" type="image/x-icon"  href="/images/flag_us.png" />
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css"/>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap-theme.min.css"/>
        <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />
        
        <style>
            body {overflow-y: scroll;}
            body.modal-open { overflow-y: scroll; margin: 0 auto;}
            .modal { overflow-y: auto; }
            #container { background: #ccc; padding: 30px; border-width:5px; border-color:black; margin: 0; box-sizing: content-box;}
            #resizable { background-position: top left;  padding: 10px; border-width:5px; margin: 0; box-sizing: content-box;}
            #resize_image { padding: 0px; border-width:0px; margin: 0; width: 100%, height: 100%} 
        </style>  
    </head>
    
    <body>
        <a href="http://github.com/wigglyworld/us_flags">
            <img style="position: absolute; top: 0; right: 0; border: 0;" src="http://s3.amazonaws.com/github/ribbons/forkme_right_gray_6d6d6d.png" 
                alt="Fork me on GitHub" />
        </a>
        
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="page-header">US State and Territory Flags <small>- Resize, reformat and download.</small></h1>
                </div>
            </div>
            
            <div class="row">
                %for item in flags:
                    <div class="col-lg-2 col-md-4 col-xs-6">
                        <div class="thumbnail" >
                            <img src="/images/us/svg/{{item}}" 
                                 alt="{{item.split('.')[0].split('_', 3)[3].replace('_', ' ')}}"
                                 style="width:150px;height:100px;"/>
                            <div class="caption">
                                <p style="text-align: center; margin-top: 0em; margin-bottom: 0em">
                                    <b>{{item.split('.')[0].split('_', 3)[3].replace('_', ' ')}}</b>
                                </p>
                                <p style="line-height:1.0;margin-top: 0em; margin-bottom: 0em">
                                    <small>
                                        <em>
                                            <a href="/images/us/svg/{{item}}" style="text-align: left;"  class="pull-left" download>SVG</a>
                                            <a href="#" data-toggle="modal" data-target="#flagModal" class="pull-right"
                                                data-flag-name="{{item.split('.')[0].split('_', 3)[3].replace('_', ' ')}}" 
                                                data-flag-image="{{item}}" data-flag-file="{{item}}">Download image
                                            </a>
                                        </em>
                                    </small>
                                </p>
                                
                            </div>
                        </div>
                    </div>
                %end

            </div>
        
            <!-- Footer -->
            <footer>
                <div class="row">
                    <div class="col-lg-12">
                        <p>Wigglyworld LLC, 2015 - An test app to evaluate cloud CI providers.</p>
                    </div>
                </div>
            </footer>
        </div>  <!-- /.container -->
        
        <div id="flagModal" class="modal fade" style="z-index: 1500;">
            <div class="modal-dialog" >
                <div class="modal-content" style="margin:0 auto;">
                    <div class="modal-header">
                        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
                        <h4 id="modal-title">TBD</h4>
                    </div>
                    <div class="modal-body" style="text-align: center;">
                        <div id="container" class="ui-widget-content" style="margin:0 auto;">
                            <div id="resizable" class="ui-widget-content">
                              <img id="resize_image" style="width:100%; height:100%;" src="None" alt="None"/>
                            </div>
                        </div>
                        <br/>
                        <div class="row">
                            <div class="col-xs-4">
                                <label class="radio-inline">
                                    <input type="radio" name="optradio" value="png" checked/>PNG
                                </label>
                                <label class="radio-inline">
                                    <input type="radio" name="optradio" value="jpg" />JPG
                                </label>
                            </div>
                            <div class="col-xs-6 pull-right">
                                <label for="dim_w">Width</label>
                                <input id="dim_w" type="text" readonly style = "width:4em;"/>
                                <label for="dim_h">Height</label>
                                <input id="dim_h" type="text" readonly style = "width:4em;"/>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
                        <a id="download_button" type="button" class="btn btn-primary">Download</a>
                    </div>
                </div>
            </div>
        </div>
	
    
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
        <script type="text/javascript" src="static/flags.js" charset="utf-8"></script>
    </body>
</html>