document.addEventListener('DOMContentLoaded', () => {
                function nav_control(){
                    hidelist = document.querySelector('#hidelist')
                    nav = document.querySelector('#hidelist');
                    if(hidelist.style.display == 'none'){
                        
                        hidelist.style.display = 'block';
                        
                    }
                    else if(hidelist.style.display == 'block' ){
                            hidelist.style.display = 'none';
                 
                        
                    }

                    else{
                       
                        hidelist.style.display = 'block';

                    }
                }
                document.querySelector('#nav_home').onclick = nav_control
                function largeScreen(mediaScreen) {
                        nav = document.querySelector('#hidelist')
                        //If screen size is more than 800px
                        if (mediaScreen.matches) { // If media query matches
                               
                                document.querySelector('#nav_home').onclick = function(){
                                    return false;
                                }
                               
                                
                        nav.style.width = '100%';
                        nav.style.display = 'flex';
                        } 
                        //else If screen size is less than 800px
                        else{
                            nav.style.display = 'none';
                            document.querySelector('#nav_home').onclick = nav_control
                        
                      
                        }
                        
                        }

                        var x = window.matchMedia("(min-width: 800px)")
                        largeScreen(x) // Call listener function at run time
                        x.addListener(largeScreen) // Attach listener function on state changes
            })