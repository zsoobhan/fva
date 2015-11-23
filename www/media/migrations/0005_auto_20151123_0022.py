# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0004_auto_20151122_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flickralbum',
            name='icon',
            field=models.CharField(default=b'fa-align-right', help_text=b'The font awesome icon to be displayed', max_length=64, choices=[(b'fa-glass', b'Glass'), (b'fa-music', b'Music'), (b'fa-search', b'Search'), (b'fa-envelope-o', b'Envelope-o'), (b'fa-heart', b'Heart'), (b'fa-star', b'Star'), (b'fa-star-o', b'Star-o'), (b'fa-user', b'User'), (b'fa-film', b'Film'), (b'fa-th-large', b'Th-large'), (b'fa-th', b'Th'), (b'fa-th-list', b'Th-list'), (b'fa-check', b'Check'), (b'fa-remove', b'Remove'), (b'fa-close', b'Close'), (b'fa-times', b'Times'), (b'fa-search-plus', b'Search-plus'), (b'fa-search-minus', b'Search-minus'), (b'fa-power-off', b'Power-off'), (b'fa-signal', b'Signal'), (b'fa-gear', b'Gear'), (b'fa-cog', b'Cog'), (b'fa-trash-o', b'Trash-o'), (b'fa-home', b'Home'), (b'fa-file-o', b'File-o'), (b'fa-clock-o', b'Clock-o'), (b'fa-road', b'Road'), (b'fa-download', b'Download'), (b'fa-arrow-circle-o-down', b'Arrow-circle-o-down'), (b'fa-arrow-circle-o-up', b'Arrow-circle-o-up'), (b'fa-inbox', b'Inbox'), (b'fa-play-circle-o', b'Play-circle-o'), (b'fa-rotate-right', b'Rotate-right'), (b'fa-repeat', b'Repeat'), (b'fa-refresh', b'Refresh'), (b'fa-list-alt', b'List-alt'), (b'fa-lock', b'Lock'), (b'fa-flag', b'Flag'), (b'fa-headphones', b'Headphones'), (b'fa-volume-off', b'Volume-off'), (b'fa-volume-down', b'Volume-down'), (b'fa-volume-up', b'Volume-up'), (b'fa-qrcode', b'Qrcode'), (b'fa-barcode', b'Barcode'), (b'fa-tag', b'Tag'), (b'fa-tags', b'Tags'), (b'fa-book', b'Book'), (b'fa-bookmark', b'Bookmark'), (b'fa-print', b'Print'), (b'fa-camera', b'Camera'), (b'fa-font', b'Font'), (b'fa-bold', b'Bold'), (b'fa-italic', b'Italic'), (b'fa-text-height', b'Text-height'), (b'fa-text-width', b'Text-width'), (b'fa-align-left', b'Align-left'), (b'fa-align-center', b'Align-center'), (b'fa-align-right', b'Align-right'), (b'fa-align-justify', b'Align-justify'), (b'fa-list', b'List'), (b'fa-dedent', b'Dedent'), (b'fa-outdent', b'Outdent'), (b'fa-indent', b'Indent'), (b'fa-video-camera', b'Video-camera'), (b'fa-photo', b'Photo'), (b'fa-image', b'Image'), (b'fa-picture-o', b'Picture-o'), (b'fa-pencil', b'Pencil'), (b'fa-map-marker', b'Map-marker'), (b'fa-adjust', b'Adjust'), (b'fa-tint', b'Tint'), (b'fa-edit', b'Edit'), (b'fa-pencil-square-o', b'Pencil-square-o'), (b'fa-share-square-o', b'Share-square-o'), (b'fa-check-square-o', b'Check-square-o'), (b'fa-arrows', b'Arrows'), (b'fa-step-backward', b'Step-backward'), (b'fa-fast-backward', b'Fast-backward'), (b'fa-backward', b'Backward'), (b'fa-play', b'Play'), (b'fa-pause', b'Pause'), (b'fa-stop', b'Stop'), (b'fa-forward', b'Forward'), (b'fa-fast-forward', b'Fast-forward'), (b'fa-step-forward', b'Step-forward'), (b'fa-eject', b'Eject'), (b'fa-chevron-left', b'Chevron-left'), (b'fa-chevron-right', b'Chevron-right'), (b'fa-plus-circle', b'Plus-circle'), (b'fa-minus-circle', b'Minus-circle'), (b'fa-times-circle', b'Times-circle'), (b'fa-check-circle', b'Check-circle'), (b'fa-question-circle', b'Question-circle'), (b'fa-info-circle', b'Info-circle'), (b'fa-crosshairs', b'Crosshairs'), (b'fa-times-circle-o', b'Times-circle-o'), (b'fa-check-circle-o', b'Check-circle-o'), (b'fa-ban', b'Ban'), (b'fa-arrow-left', b'Arrow-left'), (b'fa-arrow-right', b'Arrow-right'), (b'fa-arrow-up', b'Arrow-up'), (b'fa-arrow-down', b'Arrow-down'), (b'fa-mail-forward', b'Mail-forward'), (b'fa-share', b'Share'), (b'fa-expand', b'Expand'), (b'fa-compress', b'Compress'), (b'fa-plus', b'Plus'), (b'fa-minus', b'Minus'), (b'fa-asterisk', b'Asterisk'), (b'fa-exclamation-circle', b'Exclamation-circle'), (b'fa-gift', b'Gift'), (b'fa-leaf', b'Leaf'), (b'fa-fire', b'Fire'), (b'fa-eye', b'Eye'), (b'fa-eye-slash', b'Eye-slash'), (b'fa-warning', b'Warning'), (b'fa-exclamation-triangle', b'Exclamation-triangle'), (b'fa-plane', b'Plane'), (b'fa-calendar', b'Calendar'), (b'fa-random', b'Random'), (b'fa-comment', b'Comment'), (b'fa-magnet', b'Magnet'), (b'fa-chevron-up', b'Chevron-up'), (b'fa-chevron-down', b'Chevron-down'), (b'fa-retweet', b'Retweet'), (b'fa-shopping-cart', b'Shopping-cart'), (b'fa-folder', b'Folder'), (b'fa-folder-open', b'Folder-open'), (b'fa-arrows-v', b'Arrows-v'), (b'fa-arrows-h', b'Arrows-h'), (b'fa-bar-chart-o', b'Bar-chart-o'), (b'fa-bar-chart', b'Bar-chart'), (b'fa-twitter-square', b'Twitter-square'), (b'fa-facebook-square', b'Facebook-square'), (b'fa-camera-retro', b'Camera-retro'), (b'fa-key', b'Key'), (b'fa-gears', b'Gears'), (b'fa-cogs', b'Cogs'), (b'fa-comments', b'Comments'), (b'fa-thumbs-o-up', b'Thumbs-o-up'), (b'fa-thumbs-o-down', b'Thumbs-o-down'), (b'fa-star-half', b'Star-half'), (b'fa-heart-o', b'Heart-o'), (b'fa-sign-out', b'Sign-out'), (b'fa-linkedin-square', b'Linkedin-square'), (b'fa-thumb-tack', b'Thumb-tack'), (b'fa-external-link', b'External-link'), (b'fa-sign-in', b'Sign-in'), (b'fa-trophy', b'Trophy'), (b'fa-github-square', b'Github-square'), (b'fa-upload', b'Upload'), (b'fa-lemon-o', b'Lemon-o'), (b'fa-phone', b'Phone'), (b'fa-square-o', b'Square-o'), (b'fa-bookmark-o', b'Bookmark-o'), (b'fa-phone-square', b'Phone-square'), (b'fa-twitter', b'Twitter'), (b'fa-facebook-f', b'Facebook-f'), (b'fa-facebook', b'Facebook'), (b'fa-github', b'Github'), (b'fa-unlock', b'Unlock'), (b'fa-credit-card', b'Credit-card'), (b'fa-rss', b'Rss'), (b'fa-hdd-o', b'Hdd-o'), (b'fa-bullhorn', b'Bullhorn'), (b'fa-bell', b'Bell'), (b'fa-certificate', b'Certificate'), (b'fa-hand-o-right', b'Hand-o-right'), (b'fa-hand-o-left', b'Hand-o-left'), (b'fa-hand-o-up', b'Hand-o-up'), (b'fa-hand-o-down', b'Hand-o-down'), (b'fa-arrow-circle-left', b'Arrow-circle-left'), (b'fa-arrow-circle-right', b'Arrow-circle-right'), (b'fa-arrow-circle-up', b'Arrow-circle-up'), (b'fa-arrow-circle-down', b'Arrow-circle-down'), (b'fa-globe', b'Globe'), (b'fa-wrench', b'Wrench'), (b'fa-tasks', b'Tasks'), (b'fa-filter', b'Filter'), (b'fa-briefcase', b'Briefcase'), (b'fa-arrows-alt', b'Arrows-alt'), (b'fa-group', b'Group'), (b'fa-users', b'Users'), (b'fa-chain', b'Chain'), (b'fa-link', b'Link'), (b'fa-cloud', b'Cloud'), (b'fa-flask', b'Flask'), (b'fa-cut', b'Cut'), (b'fa-scissors', b'Scissors'), (b'fa-copy', b'Copy'), (b'fa-files-o', b'Files-o'), (b'fa-paperclip', b'Paperclip'), (b'fa-save', b'Save'), (b'fa-floppy-o', b'Floppy-o'), (b'fa-square', b'Square'), (b'fa-navicon', b'Navicon'), (b'fa-reorder', b'Reorder'), (b'fa-bars', b'Bars'), (b'fa-list-ul', b'List-ul'), (b'fa-list-ol', b'List-ol'), (b'fa-strikethrough', b'Strikethrough'), (b'fa-underline', b'Underline'), (b'fa-table', b'Table'), (b'fa-magic', b'Magic'), (b'fa-truck', b'Truck'), (b'fa-pinterest', b'Pinterest'), (b'fa-pinterest-square', b'Pinterest-square'), (b'fa-google-plus-square', b'Google-plus-square'), (b'fa-google-plus', b'Google-plus'), (b'fa-money', b'Money'), (b'fa-caret-down', b'Caret-down'), (b'fa-caret-up', b'Caret-up'), (b'fa-caret-left', b'Caret-left'), (b'fa-caret-right', b'Caret-right'), (b'fa-columns', b'Columns'), (b'fa-unsorted', b'Unsorted'), (b'fa-sort', b'Sort'), (b'fa-sort-down', b'Sort-down'), (b'fa-sort-desc', b'Sort-desc'), (b'fa-sort-up', b'Sort-up'), (b'fa-sort-asc', b'Sort-asc'), (b'fa-envelope', b'Envelope'), (b'fa-linkedin', b'Linkedin'), (b'fa-rotate-left', b'Rotate-left'), (b'fa-undo', b'Undo'), (b'fa-legal', b'Legal'), (b'fa-gavel', b'Gavel'), (b'fa-dashboard', b'Dashboard'), (b'fa-tachometer', b'Tachometer'), (b'fa-comment-o', b'Comment-o'), (b'fa-comments-o', b'Comments-o'), (b'fa-flash', b'Flash'), (b'fa-bolt', b'Bolt'), (b'fa-sitemap', b'Sitemap'), (b'fa-umbrella', b'Umbrella'), (b'fa-paste', b'Paste'), (b'fa-clipboard', b'Clipboard'), (b'fa-lightbulb-o', b'Lightbulb-o'), (b'fa-exchange', b'Exchange'), (b'fa-cloud-download', b'Cloud-download'), (b'fa-cloud-upload', b'Cloud-upload'), (b'fa-user-md', b'User-md'), (b'fa-stethoscope', b'Stethoscope'), (b'fa-suitcase', b'Suitcase'), (b'fa-bell-o', b'Bell-o'), (b'fa-coffee', b'Coffee'), (b'fa-cutlery', b'Cutlery'), (b'fa-file-text-o', b'File-text-o'), (b'fa-building-o', b'Building-o'), (b'fa-hospital-o', b'Hospital-o'), (b'fa-ambulance', b'Ambulance'), (b'fa-medkit', b'Medkit'), (b'fa-fighter-jet', b'Fighter-jet'), (b'fa-beer', b'Beer'), (b'fa-h-square', b'H-square'), (b'fa-plus-square', b'Plus-square'), (b'fa-angle-double-left', b'Angle-double-left'), (b'fa-angle-double-right', b'Angle-double-right'), (b'fa-angle-double-up', b'Angle-double-up'), (b'fa-angle-double-down', b'Angle-double-down'), (b'fa-angle-left', b'Angle-left'), (b'fa-angle-right', b'Angle-right'), (b'fa-angle-up', b'Angle-up'), (b'fa-angle-down', b'Angle-down'), (b'fa-desktop', b'Desktop'), (b'fa-laptop', b'Laptop'), (b'fa-tablet', b'Tablet'), (b'fa-mobile-phone', b'Mobile-phone'), (b'fa-mobile', b'Mobile'), (b'fa-circle-o', b'Circle-o'), (b'fa-quote-left', b'Quote-left'), (b'fa-quote-right', b'Quote-right'), (b'fa-spinner', b'Spinner'), (b'fa-circle', b'Circle'), (b'fa-mail-reply', b'Mail-reply'), (b'fa-reply', b'Reply'), (b'fa-github-alt', b'Github-alt'), (b'fa-folder-o', b'Folder-o'), (b'fa-folder-open-o', b'Folder-open-o'), (b'fa-smile-o', b'Smile-o'), (b'fa-frown-o', b'Frown-o'), (b'fa-meh-o', b'Meh-o'), (b'fa-gamepad', b'Gamepad'), (b'fa-keyboard-o', b'Keyboard-o'), (b'fa-flag-o', b'Flag-o'), (b'fa-flag-checkered', b'Flag-checkered'), (b'fa-terminal', b'Terminal'), (b'fa-code', b'Code'), (b'fa-mail-reply-all', b'Mail-reply-all'), (b'fa-reply-all', b'Reply-all'), (b'fa-star-half-empty', b'Star-half-empty'), (b'fa-star-half-full', b'Star-half-full'), (b'fa-star-half-o', b'Star-half-o'), (b'fa-location-arrow', b'Location-arrow'), (b'fa-crop', b'Crop'), (b'fa-code-fork', b'Code-fork'), (b'fa-unlink', b'Unlink'), (b'fa-chain-broken', b'Chain-broken'), (b'fa-question', b'Question'), (b'fa-info', b'Info'), (b'fa-exclamation', b'Exclamation'), (b'fa-superscript', b'Superscript'), (b'fa-subscript', b'Subscript'), (b'fa-eraser', b'Eraser'), (b'fa-puzzle-piece', b'Puzzle-piece'), (b'fa-microphone', b'Microphone'), (b'fa-microphone-slash', b'Microphone-slash'), (b'fa-shield', b'Shield'), (b'fa-calendar-o', b'Calendar-o'), (b'fa-fire-extinguisher', b'Fire-extinguisher'), (b'fa-rocket', b'Rocket'), (b'fa-maxcdn', b'Maxcdn'), (b'fa-chevron-circle-left', b'Chevron-circle-left'), (b'fa-chevron-circle-right', b'Chevron-circle-right'), (b'fa-chevron-circle-up', b'Chevron-circle-up'), (b'fa-chevron-circle-down', b'Chevron-circle-down'), (b'fa-html5', b'Html5'), (b'fa-css3', b'Css3'), (b'fa-anchor', b'Anchor'), (b'fa-unlock-alt', b'Unlock-alt'), (b'fa-bullseye', b'Bullseye'), (b'fa-ellipsis-h', b'Ellipsis-h'), (b'fa-ellipsis-v', b'Ellipsis-v'), (b'fa-rss-square', b'Rss-square'), (b'fa-play-circle', b'Play-circle'), (b'fa-ticket', b'Ticket'), (b'fa-minus-square', b'Minus-square'), (b'fa-minus-square-o', b'Minus-square-o'), (b'fa-level-up', b'Level-up'), (b'fa-level-down', b'Level-down'), (b'fa-check-square', b'Check-square'), (b'fa-pencil-square', b'Pencil-square'), (b'fa-external-link-square', b'External-link-square'), (b'fa-share-square', b'Share-square'), (b'fa-compass', b'Compass'), (b'fa-toggle-down', b'Toggle-down'), (b'fa-caret-square-o-down', b'Caret-square-o-down'), (b'fa-toggle-up', b'Toggle-up'), (b'fa-caret-square-o-up', b'Caret-square-o-up'), (b'fa-toggle-right', b'Toggle-right'), (b'fa-caret-square-o-right', b'Caret-square-o-right'), (b'fa-euro', b'Euro'), (b'fa-eur', b'Eur'), (b'fa-gbp', b'Gbp'), (b'fa-dollar', b'Dollar'), (b'fa-usd', b'Usd'), (b'fa-rupee', b'Rupee'), (b'fa-inr', b'Inr'), (b'fa-cny', b'Cny'), (b'fa-rmb', b'Rmb'), (b'fa-yen', b'Yen'), (b'fa-jpy', b'Jpy'), (b'fa-ruble', b'Ruble'), (b'fa-rouble', b'Rouble'), (b'fa-rub', b'Rub'), (b'fa-won', b'Won'), (b'fa-krw', b'Krw'), (b'fa-bitcoin', b'Bitcoin'), (b'fa-btc', b'Btc'), (b'fa-file', b'File'), (b'fa-file-text', b'File-text'), (b'fa-sort-alpha-asc', b'Sort-alpha-asc'), (b'fa-sort-alpha-desc', b'Sort-alpha-desc'), (b'fa-sort-amount-asc', b'Sort-amount-asc'), (b'fa-sort-amount-desc', b'Sort-amount-desc'), (b'fa-sort-numeric-asc', b'Sort-numeric-asc'), (b'fa-sort-numeric-desc', b'Sort-numeric-desc'), (b'fa-thumbs-up', b'Thumbs-up'), (b'fa-thumbs-down', b'Thumbs-down'), (b'fa-youtube-square', b'Youtube-square'), (b'fa-youtube', b'Youtube'), (b'fa-xing', b'Xing'), (b'fa-xing-square', b'Xing-square'), (b'fa-youtube-play', b'Youtube-play'), (b'fa-dropbox', b'Dropbox'), (b'fa-stack-overflow', b'Stack-overflow'), (b'fa-instagram', b'Instagram'), (b'fa-flickr', b'Flickr'), (b'fa-adn', b'Adn'), (b'fa-bitbucket', b'Bitbucket'), (b'fa-bitbucket-square', b'Bitbucket-square'), (b'fa-tumblr', b'Tumblr'), (b'fa-tumblr-square', b'Tumblr-square'), (b'fa-long-arrow-down', b'Long-arrow-down'), (b'fa-long-arrow-up', b'Long-arrow-up'), (b'fa-long-arrow-left', b'Long-arrow-left'), (b'fa-long-arrow-right', b'Long-arrow-right'), (b'fa-apple', b'Apple'), (b'fa-windows', b'Windows'), (b'fa-android', b'Android'), (b'fa-linux', b'Linux'), (b'fa-dribbble', b'Dribbble'), (b'fa-skype', b'Skype'), (b'fa-foursquare', b'Foursquare'), (b'fa-trello', b'Trello'), (b'fa-female', b'Female'), (b'fa-male', b'Male'), (b'fa-gittip', b'Gittip'), (b'fa-gratipay', b'Gratipay'), (b'fa-sun-o', b'Sun-o'), (b'fa-moon-o', b'Moon-o'), (b'fa-archive', b'Archive'), (b'fa-bug', b'Bug'), (b'fa-vk', b'Vk'), (b'fa-weibo', b'Weibo'), (b'fa-renren', b'Renren'), (b'fa-pagelines', b'Pagelines'), (b'fa-stack-exchange', b'Stack-exchange'), (b'fa-arrow-circle-o-right', b'Arrow-circle-o-right'), (b'fa-arrow-circle-o-left', b'Arrow-circle-o-left'), (b'fa-toggle-left', b'Toggle-left'), (b'fa-caret-square-o-left', b'Caret-square-o-left'), (b'fa-dot-circle-o', b'Dot-circle-o'), (b'fa-wheelchair', b'Wheelchair'), (b'fa-vimeo-square', b'Vimeo-square'), (b'fa-turkish-lira', b'Turkish-lira'), (b'fa-try', b'Try'), (b'fa-plus-square-o', b'Plus-square-o'), (b'fa-space-shuttle', b'Space-shuttle'), (b'fa-slack', b'Slack'), (b'fa-envelope-square', b'Envelope-square'), (b'fa-wordpress', b'Wordpress'), (b'fa-openid', b'Openid'), (b'fa-institution', b'Institution'), (b'fa-bank', b'Bank'), (b'fa-university', b'University'), (b'fa-mortar-board', b'Mortar-board'), (b'fa-graduation-cap', b'Graduation-cap'), (b'fa-yahoo', b'Yahoo'), (b'fa-google', b'Google'), (b'fa-reddit', b'Reddit'), (b'fa-reddit-square', b'Reddit-square'), (b'fa-stumbleupon-circle', b'Stumbleupon-circle'), (b'fa-stumbleupon', b'Stumbleupon'), (b'fa-delicious', b'Delicious'), (b'fa-digg', b'Digg'), (b'fa-pied-piper', b'Pied-piper'), (b'fa-pied-piper-alt', b'Pied-piper-alt'), (b'fa-drupal', b'Drupal'), (b'fa-joomla', b'Joomla'), (b'fa-language', b'Language'), (b'fa-fax', b'Fax'), (b'fa-building', b'Building'), (b'fa-child', b'Child'), (b'fa-paw', b'Paw'), (b'fa-spoon', b'Spoon'), (b'fa-cube', b'Cube'), (b'fa-cubes', b'Cubes'), (b'fa-behance', b'Behance'), (b'fa-behance-square', b'Behance-square'), (b'fa-steam', b'Steam'), (b'fa-steam-square', b'Steam-square'), (b'fa-recycle', b'Recycle'), (b'fa-automobile', b'Automobile'), (b'fa-car', b'Car'), (b'fa-cab', b'Cab'), (b'fa-taxi', b'Taxi'), (b'fa-tree', b'Tree'), (b'fa-spotify', b'Spotify'), (b'fa-deviantart', b'Deviantart'), (b'fa-soundcloud', b'Soundcloud'), (b'fa-database', b'Database'), (b'fa-file-pdf-o', b'File-pdf-o'), (b'fa-file-word-o', b'File-word-o'), (b'fa-file-excel-o', b'File-excel-o'), (b'fa-file-powerpoint-o', b'File-powerpoint-o'), (b'fa-file-photo-o', b'File-photo-o'), (b'fa-file-picture-o', b'File-picture-o'), (b'fa-file-image-o', b'File-image-o'), (b'fa-file-zip-o', b'File-zip-o'), (b'fa-file-archive-o', b'File-archive-o'), (b'fa-file-sound-o', b'File-sound-o'), (b'fa-file-audio-o', b'File-audio-o'), (b'fa-file-movie-o', b'File-movie-o'), (b'fa-file-video-o', b'File-video-o'), (b'fa-file-code-o', b'File-code-o'), (b'fa-vine', b'Vine'), (b'fa-codepen', b'Codepen'), (b'fa-jsfiddle', b'Jsfiddle'), (b'fa-life-bouy', b'Life-bouy'), (b'fa-life-buoy', b'Life-buoy'), (b'fa-life-saver', b'Life-saver'), (b'fa-support', b'Support'), (b'fa-life-ring', b'Life-ring'), (b'fa-circle-o-notch', b'Circle-o-notch'), (b'fa-ra', b'Ra'), (b'fa-rebel', b'Rebel'), (b'fa-ge', b'Ge'), (b'fa-empire', b'Empire'), (b'fa-git-square', b'Git-square'), (b'fa-git', b'Git'), (b'fa-hacker-news', b'Hacker-news'), (b'fa-tencent-weibo', b'Tencent-weibo'), (b'fa-qq', b'Qq'), (b'fa-wechat', b'Wechat'), (b'fa-weixin', b'Weixin'), (b'fa-send', b'Send'), (b'fa-paper-plane', b'Paper-plane'), (b'fa-send-o', b'Send-o'), (b'fa-paper-plane-o', b'Paper-plane-o'), (b'fa-history', b'History'), (b'fa-genderless', b'Genderless'), (b'fa-circle-thin', b'Circle-thin'), (b'fa-header', b'Header'), (b'fa-paragraph', b'Paragraph'), (b'fa-sliders', b'Sliders'), (b'fa-share-alt', b'Share-alt'), (b'fa-share-alt-square', b'Share-alt-square'), (b'fa-bomb', b'Bomb'), (b'fa-soccer-ball-o', b'Soccer-ball-o'), (b'fa-futbol-o', b'Futbol-o'), (b'fa-tty', b'Tty'), (b'fa-binoculars', b'Binoculars'), (b'fa-plug', b'Plug'), (b'fa-slideshare', b'Slideshare'), (b'fa-twitch', b'Twitch'), (b'fa-yelp', b'Yelp'), (b'fa-newspaper-o', b'Newspaper-o'), (b'fa-wifi', b'Wifi'), (b'fa-calculator', b'Calculator'), (b'fa-paypal', b'Paypal'), (b'fa-google-wallet', b'Google-wallet'), (b'fa-cc-visa', b'Cc-visa'), (b'fa-cc-mastercard', b'Cc-mastercard'), (b'fa-cc-discover', b'Cc-discover'), (b'fa-cc-amex', b'Cc-amex'), (b'fa-cc-paypal', b'Cc-paypal'), (b'fa-cc-stripe', b'Cc-stripe'), (b'fa-bell-slash', b'Bell-slash'), (b'fa-bell-slash-o', b'Bell-slash-o'), (b'fa-trash', b'Trash'), (b'fa-copyright', b'Copyright'), (b'fa-at', b'At'), (b'fa-eyedropper', b'Eyedropper'), (b'fa-paint-brush', b'Paint-brush'), (b'fa-birthday-cake', b'Birthday-cake'), (b'fa-area-chart', b'Area-chart'), (b'fa-pie-chart', b'Pie-chart'), (b'fa-line-chart', b'Line-chart'), (b'fa-lastfm', b'Lastfm'), (b'fa-lastfm-square', b'Lastfm-square'), (b'fa-toggle-off', b'Toggle-off'), (b'fa-toggle-on', b'Toggle-on'), (b'fa-bicycle', b'Bicycle'), (b'fa-bus', b'Bus'), (b'fa-ioxhost', b'Ioxhost'), (b'fa-angellist', b'Angellist'), (b'fa-cc', b'Cc'), (b'fa-shekel', b'Shekel'), (b'fa-sheqel', b'Sheqel'), (b'fa-ils', b'Ils'), (b'fa-meanpath', b'Meanpath'), (b'fa-buysellads', b'Buysellads'), (b'fa-connectdevelop', b'Connectdevelop'), (b'fa-dashcube', b'Dashcube'), (b'fa-forumbee', b'Forumbee'), (b'fa-leanpub', b'Leanpub'), (b'fa-sellsy', b'Sellsy'), (b'fa-shirtsinbulk', b'Shirtsinbulk'), (b'fa-simplybuilt', b'Simplybuilt'), (b'fa-skyatlas', b'Skyatlas'), (b'fa-cart-plus', b'Cart-plus'), (b'fa-cart-arrow-down', b'Cart-arrow-down'), (b'fa-diamond', b'Diamond'), (b'fa-ship', b'Ship'), (b'fa-user-secret', b'User-secret'), (b'fa-motorcycle', b'Motorcycle'), (b'fa-street-view', b'Street-view'), (b'fa-heartbeat', b'Heartbeat'), (b'fa-venus', b'Venus'), (b'fa-mars', b'Mars'), (b'fa-mercury', b'Mercury'), (b'fa-transgender', b'Transgender'), (b'fa-transgender-alt', b'Transgender-alt'), (b'fa-venus-double', b'Venus-double'), (b'fa-mars-double', b'Mars-double'), (b'fa-venus-mars', b'Venus-mars'), (b'fa-mars-stroke', b'Mars-stroke'), (b'fa-mars-stroke-v', b'Mars-stroke-v'), (b'fa-mars-stroke-h', b'Mars-stroke-h'), (b'fa-neuter', b'Neuter'), (b'fa-facebook-official', b'Facebook-official'), (b'fa-pinterest-p', b'Pinterest-p'), (b'fa-whatsapp', b'Whatsapp'), (b'fa-server', b'Server'), (b'fa-user-plus', b'User-plus'), (b'fa-user-times', b'User-times'), (b'fa-hotel', b'Hotel'), (b'fa-bed', b'Bed'), (b'fa-viacoin', b'Viacoin'), (b'fa-train', b'Train'), (b'fa-subway', b'Subway'), (b'fa-medium', b'Medium')]),
        ),
        migrations.AlterField(
            model_name='youtubevideo',
            name='icon',
            field=models.CharField(default=b'fa-align-right', help_text=b'The font awesome icon to be displayed', max_length=64, choices=[(b'fa-glass', b'Glass'), (b'fa-music', b'Music'), (b'fa-search', b'Search'), (b'fa-envelope-o', b'Envelope-o'), (b'fa-heart', b'Heart'), (b'fa-star', b'Star'), (b'fa-star-o', b'Star-o'), (b'fa-user', b'User'), (b'fa-film', b'Film'), (b'fa-th-large', b'Th-large'), (b'fa-th', b'Th'), (b'fa-th-list', b'Th-list'), (b'fa-check', b'Check'), (b'fa-remove', b'Remove'), (b'fa-close', b'Close'), (b'fa-times', b'Times'), (b'fa-search-plus', b'Search-plus'), (b'fa-search-minus', b'Search-minus'), (b'fa-power-off', b'Power-off'), (b'fa-signal', b'Signal'), (b'fa-gear', b'Gear'), (b'fa-cog', b'Cog'), (b'fa-trash-o', b'Trash-o'), (b'fa-home', b'Home'), (b'fa-file-o', b'File-o'), (b'fa-clock-o', b'Clock-o'), (b'fa-road', b'Road'), (b'fa-download', b'Download'), (b'fa-arrow-circle-o-down', b'Arrow-circle-o-down'), (b'fa-arrow-circle-o-up', b'Arrow-circle-o-up'), (b'fa-inbox', b'Inbox'), (b'fa-play-circle-o', b'Play-circle-o'), (b'fa-rotate-right', b'Rotate-right'), (b'fa-repeat', b'Repeat'), (b'fa-refresh', b'Refresh'), (b'fa-list-alt', b'List-alt'), (b'fa-lock', b'Lock'), (b'fa-flag', b'Flag'), (b'fa-headphones', b'Headphones'), (b'fa-volume-off', b'Volume-off'), (b'fa-volume-down', b'Volume-down'), (b'fa-volume-up', b'Volume-up'), (b'fa-qrcode', b'Qrcode'), (b'fa-barcode', b'Barcode'), (b'fa-tag', b'Tag'), (b'fa-tags', b'Tags'), (b'fa-book', b'Book'), (b'fa-bookmark', b'Bookmark'), (b'fa-print', b'Print'), (b'fa-camera', b'Camera'), (b'fa-font', b'Font'), (b'fa-bold', b'Bold'), (b'fa-italic', b'Italic'), (b'fa-text-height', b'Text-height'), (b'fa-text-width', b'Text-width'), (b'fa-align-left', b'Align-left'), (b'fa-align-center', b'Align-center'), (b'fa-align-right', b'Align-right'), (b'fa-align-justify', b'Align-justify'), (b'fa-list', b'List'), (b'fa-dedent', b'Dedent'), (b'fa-outdent', b'Outdent'), (b'fa-indent', b'Indent'), (b'fa-video-camera', b'Video-camera'), (b'fa-photo', b'Photo'), (b'fa-image', b'Image'), (b'fa-picture-o', b'Picture-o'), (b'fa-pencil', b'Pencil'), (b'fa-map-marker', b'Map-marker'), (b'fa-adjust', b'Adjust'), (b'fa-tint', b'Tint'), (b'fa-edit', b'Edit'), (b'fa-pencil-square-o', b'Pencil-square-o'), (b'fa-share-square-o', b'Share-square-o'), (b'fa-check-square-o', b'Check-square-o'), (b'fa-arrows', b'Arrows'), (b'fa-step-backward', b'Step-backward'), (b'fa-fast-backward', b'Fast-backward'), (b'fa-backward', b'Backward'), (b'fa-play', b'Play'), (b'fa-pause', b'Pause'), (b'fa-stop', b'Stop'), (b'fa-forward', b'Forward'), (b'fa-fast-forward', b'Fast-forward'), (b'fa-step-forward', b'Step-forward'), (b'fa-eject', b'Eject'), (b'fa-chevron-left', b'Chevron-left'), (b'fa-chevron-right', b'Chevron-right'), (b'fa-plus-circle', b'Plus-circle'), (b'fa-minus-circle', b'Minus-circle'), (b'fa-times-circle', b'Times-circle'), (b'fa-check-circle', b'Check-circle'), (b'fa-question-circle', b'Question-circle'), (b'fa-info-circle', b'Info-circle'), (b'fa-crosshairs', b'Crosshairs'), (b'fa-times-circle-o', b'Times-circle-o'), (b'fa-check-circle-o', b'Check-circle-o'), (b'fa-ban', b'Ban'), (b'fa-arrow-left', b'Arrow-left'), (b'fa-arrow-right', b'Arrow-right'), (b'fa-arrow-up', b'Arrow-up'), (b'fa-arrow-down', b'Arrow-down'), (b'fa-mail-forward', b'Mail-forward'), (b'fa-share', b'Share'), (b'fa-expand', b'Expand'), (b'fa-compress', b'Compress'), (b'fa-plus', b'Plus'), (b'fa-minus', b'Minus'), (b'fa-asterisk', b'Asterisk'), (b'fa-exclamation-circle', b'Exclamation-circle'), (b'fa-gift', b'Gift'), (b'fa-leaf', b'Leaf'), (b'fa-fire', b'Fire'), (b'fa-eye', b'Eye'), (b'fa-eye-slash', b'Eye-slash'), (b'fa-warning', b'Warning'), (b'fa-exclamation-triangle', b'Exclamation-triangle'), (b'fa-plane', b'Plane'), (b'fa-calendar', b'Calendar'), (b'fa-random', b'Random'), (b'fa-comment', b'Comment'), (b'fa-magnet', b'Magnet'), (b'fa-chevron-up', b'Chevron-up'), (b'fa-chevron-down', b'Chevron-down'), (b'fa-retweet', b'Retweet'), (b'fa-shopping-cart', b'Shopping-cart'), (b'fa-folder', b'Folder'), (b'fa-folder-open', b'Folder-open'), (b'fa-arrows-v', b'Arrows-v'), (b'fa-arrows-h', b'Arrows-h'), (b'fa-bar-chart-o', b'Bar-chart-o'), (b'fa-bar-chart', b'Bar-chart'), (b'fa-twitter-square', b'Twitter-square'), (b'fa-facebook-square', b'Facebook-square'), (b'fa-camera-retro', b'Camera-retro'), (b'fa-key', b'Key'), (b'fa-gears', b'Gears'), (b'fa-cogs', b'Cogs'), (b'fa-comments', b'Comments'), (b'fa-thumbs-o-up', b'Thumbs-o-up'), (b'fa-thumbs-o-down', b'Thumbs-o-down'), (b'fa-star-half', b'Star-half'), (b'fa-heart-o', b'Heart-o'), (b'fa-sign-out', b'Sign-out'), (b'fa-linkedin-square', b'Linkedin-square'), (b'fa-thumb-tack', b'Thumb-tack'), (b'fa-external-link', b'External-link'), (b'fa-sign-in', b'Sign-in'), (b'fa-trophy', b'Trophy'), (b'fa-github-square', b'Github-square'), (b'fa-upload', b'Upload'), (b'fa-lemon-o', b'Lemon-o'), (b'fa-phone', b'Phone'), (b'fa-square-o', b'Square-o'), (b'fa-bookmark-o', b'Bookmark-o'), (b'fa-phone-square', b'Phone-square'), (b'fa-twitter', b'Twitter'), (b'fa-facebook-f', b'Facebook-f'), (b'fa-facebook', b'Facebook'), (b'fa-github', b'Github'), (b'fa-unlock', b'Unlock'), (b'fa-credit-card', b'Credit-card'), (b'fa-rss', b'Rss'), (b'fa-hdd-o', b'Hdd-o'), (b'fa-bullhorn', b'Bullhorn'), (b'fa-bell', b'Bell'), (b'fa-certificate', b'Certificate'), (b'fa-hand-o-right', b'Hand-o-right'), (b'fa-hand-o-left', b'Hand-o-left'), (b'fa-hand-o-up', b'Hand-o-up'), (b'fa-hand-o-down', b'Hand-o-down'), (b'fa-arrow-circle-left', b'Arrow-circle-left'), (b'fa-arrow-circle-right', b'Arrow-circle-right'), (b'fa-arrow-circle-up', b'Arrow-circle-up'), (b'fa-arrow-circle-down', b'Arrow-circle-down'), (b'fa-globe', b'Globe'), (b'fa-wrench', b'Wrench'), (b'fa-tasks', b'Tasks'), (b'fa-filter', b'Filter'), (b'fa-briefcase', b'Briefcase'), (b'fa-arrows-alt', b'Arrows-alt'), (b'fa-group', b'Group'), (b'fa-users', b'Users'), (b'fa-chain', b'Chain'), (b'fa-link', b'Link'), (b'fa-cloud', b'Cloud'), (b'fa-flask', b'Flask'), (b'fa-cut', b'Cut'), (b'fa-scissors', b'Scissors'), (b'fa-copy', b'Copy'), (b'fa-files-o', b'Files-o'), (b'fa-paperclip', b'Paperclip'), (b'fa-save', b'Save'), (b'fa-floppy-o', b'Floppy-o'), (b'fa-square', b'Square'), (b'fa-navicon', b'Navicon'), (b'fa-reorder', b'Reorder'), (b'fa-bars', b'Bars'), (b'fa-list-ul', b'List-ul'), (b'fa-list-ol', b'List-ol'), (b'fa-strikethrough', b'Strikethrough'), (b'fa-underline', b'Underline'), (b'fa-table', b'Table'), (b'fa-magic', b'Magic'), (b'fa-truck', b'Truck'), (b'fa-pinterest', b'Pinterest'), (b'fa-pinterest-square', b'Pinterest-square'), (b'fa-google-plus-square', b'Google-plus-square'), (b'fa-google-plus', b'Google-plus'), (b'fa-money', b'Money'), (b'fa-caret-down', b'Caret-down'), (b'fa-caret-up', b'Caret-up'), (b'fa-caret-left', b'Caret-left'), (b'fa-caret-right', b'Caret-right'), (b'fa-columns', b'Columns'), (b'fa-unsorted', b'Unsorted'), (b'fa-sort', b'Sort'), (b'fa-sort-down', b'Sort-down'), (b'fa-sort-desc', b'Sort-desc'), (b'fa-sort-up', b'Sort-up'), (b'fa-sort-asc', b'Sort-asc'), (b'fa-envelope', b'Envelope'), (b'fa-linkedin', b'Linkedin'), (b'fa-rotate-left', b'Rotate-left'), (b'fa-undo', b'Undo'), (b'fa-legal', b'Legal'), (b'fa-gavel', b'Gavel'), (b'fa-dashboard', b'Dashboard'), (b'fa-tachometer', b'Tachometer'), (b'fa-comment-o', b'Comment-o'), (b'fa-comments-o', b'Comments-o'), (b'fa-flash', b'Flash'), (b'fa-bolt', b'Bolt'), (b'fa-sitemap', b'Sitemap'), (b'fa-umbrella', b'Umbrella'), (b'fa-paste', b'Paste'), (b'fa-clipboard', b'Clipboard'), (b'fa-lightbulb-o', b'Lightbulb-o'), (b'fa-exchange', b'Exchange'), (b'fa-cloud-download', b'Cloud-download'), (b'fa-cloud-upload', b'Cloud-upload'), (b'fa-user-md', b'User-md'), (b'fa-stethoscope', b'Stethoscope'), (b'fa-suitcase', b'Suitcase'), (b'fa-bell-o', b'Bell-o'), (b'fa-coffee', b'Coffee'), (b'fa-cutlery', b'Cutlery'), (b'fa-file-text-o', b'File-text-o'), (b'fa-building-o', b'Building-o'), (b'fa-hospital-o', b'Hospital-o'), (b'fa-ambulance', b'Ambulance'), (b'fa-medkit', b'Medkit'), (b'fa-fighter-jet', b'Fighter-jet'), (b'fa-beer', b'Beer'), (b'fa-h-square', b'H-square'), (b'fa-plus-square', b'Plus-square'), (b'fa-angle-double-left', b'Angle-double-left'), (b'fa-angle-double-right', b'Angle-double-right'), (b'fa-angle-double-up', b'Angle-double-up'), (b'fa-angle-double-down', b'Angle-double-down'), (b'fa-angle-left', b'Angle-left'), (b'fa-angle-right', b'Angle-right'), (b'fa-angle-up', b'Angle-up'), (b'fa-angle-down', b'Angle-down'), (b'fa-desktop', b'Desktop'), (b'fa-laptop', b'Laptop'), (b'fa-tablet', b'Tablet'), (b'fa-mobile-phone', b'Mobile-phone'), (b'fa-mobile', b'Mobile'), (b'fa-circle-o', b'Circle-o'), (b'fa-quote-left', b'Quote-left'), (b'fa-quote-right', b'Quote-right'), (b'fa-spinner', b'Spinner'), (b'fa-circle', b'Circle'), (b'fa-mail-reply', b'Mail-reply'), (b'fa-reply', b'Reply'), (b'fa-github-alt', b'Github-alt'), (b'fa-folder-o', b'Folder-o'), (b'fa-folder-open-o', b'Folder-open-o'), (b'fa-smile-o', b'Smile-o'), (b'fa-frown-o', b'Frown-o'), (b'fa-meh-o', b'Meh-o'), (b'fa-gamepad', b'Gamepad'), (b'fa-keyboard-o', b'Keyboard-o'), (b'fa-flag-o', b'Flag-o'), (b'fa-flag-checkered', b'Flag-checkered'), (b'fa-terminal', b'Terminal'), (b'fa-code', b'Code'), (b'fa-mail-reply-all', b'Mail-reply-all'), (b'fa-reply-all', b'Reply-all'), (b'fa-star-half-empty', b'Star-half-empty'), (b'fa-star-half-full', b'Star-half-full'), (b'fa-star-half-o', b'Star-half-o'), (b'fa-location-arrow', b'Location-arrow'), (b'fa-crop', b'Crop'), (b'fa-code-fork', b'Code-fork'), (b'fa-unlink', b'Unlink'), (b'fa-chain-broken', b'Chain-broken'), (b'fa-question', b'Question'), (b'fa-info', b'Info'), (b'fa-exclamation', b'Exclamation'), (b'fa-superscript', b'Superscript'), (b'fa-subscript', b'Subscript'), (b'fa-eraser', b'Eraser'), (b'fa-puzzle-piece', b'Puzzle-piece'), (b'fa-microphone', b'Microphone'), (b'fa-microphone-slash', b'Microphone-slash'), (b'fa-shield', b'Shield'), (b'fa-calendar-o', b'Calendar-o'), (b'fa-fire-extinguisher', b'Fire-extinguisher'), (b'fa-rocket', b'Rocket'), (b'fa-maxcdn', b'Maxcdn'), (b'fa-chevron-circle-left', b'Chevron-circle-left'), (b'fa-chevron-circle-right', b'Chevron-circle-right'), (b'fa-chevron-circle-up', b'Chevron-circle-up'), (b'fa-chevron-circle-down', b'Chevron-circle-down'), (b'fa-html5', b'Html5'), (b'fa-css3', b'Css3'), (b'fa-anchor', b'Anchor'), (b'fa-unlock-alt', b'Unlock-alt'), (b'fa-bullseye', b'Bullseye'), (b'fa-ellipsis-h', b'Ellipsis-h'), (b'fa-ellipsis-v', b'Ellipsis-v'), (b'fa-rss-square', b'Rss-square'), (b'fa-play-circle', b'Play-circle'), (b'fa-ticket', b'Ticket'), (b'fa-minus-square', b'Minus-square'), (b'fa-minus-square-o', b'Minus-square-o'), (b'fa-level-up', b'Level-up'), (b'fa-level-down', b'Level-down'), (b'fa-check-square', b'Check-square'), (b'fa-pencil-square', b'Pencil-square'), (b'fa-external-link-square', b'External-link-square'), (b'fa-share-square', b'Share-square'), (b'fa-compass', b'Compass'), (b'fa-toggle-down', b'Toggle-down'), (b'fa-caret-square-o-down', b'Caret-square-o-down'), (b'fa-toggle-up', b'Toggle-up'), (b'fa-caret-square-o-up', b'Caret-square-o-up'), (b'fa-toggle-right', b'Toggle-right'), (b'fa-caret-square-o-right', b'Caret-square-o-right'), (b'fa-euro', b'Euro'), (b'fa-eur', b'Eur'), (b'fa-gbp', b'Gbp'), (b'fa-dollar', b'Dollar'), (b'fa-usd', b'Usd'), (b'fa-rupee', b'Rupee'), (b'fa-inr', b'Inr'), (b'fa-cny', b'Cny'), (b'fa-rmb', b'Rmb'), (b'fa-yen', b'Yen'), (b'fa-jpy', b'Jpy'), (b'fa-ruble', b'Ruble'), (b'fa-rouble', b'Rouble'), (b'fa-rub', b'Rub'), (b'fa-won', b'Won'), (b'fa-krw', b'Krw'), (b'fa-bitcoin', b'Bitcoin'), (b'fa-btc', b'Btc'), (b'fa-file', b'File'), (b'fa-file-text', b'File-text'), (b'fa-sort-alpha-asc', b'Sort-alpha-asc'), (b'fa-sort-alpha-desc', b'Sort-alpha-desc'), (b'fa-sort-amount-asc', b'Sort-amount-asc'), (b'fa-sort-amount-desc', b'Sort-amount-desc'), (b'fa-sort-numeric-asc', b'Sort-numeric-asc'), (b'fa-sort-numeric-desc', b'Sort-numeric-desc'), (b'fa-thumbs-up', b'Thumbs-up'), (b'fa-thumbs-down', b'Thumbs-down'), (b'fa-youtube-square', b'Youtube-square'), (b'fa-youtube', b'Youtube'), (b'fa-xing', b'Xing'), (b'fa-xing-square', b'Xing-square'), (b'fa-youtube-play', b'Youtube-play'), (b'fa-dropbox', b'Dropbox'), (b'fa-stack-overflow', b'Stack-overflow'), (b'fa-instagram', b'Instagram'), (b'fa-flickr', b'Flickr'), (b'fa-adn', b'Adn'), (b'fa-bitbucket', b'Bitbucket'), (b'fa-bitbucket-square', b'Bitbucket-square'), (b'fa-tumblr', b'Tumblr'), (b'fa-tumblr-square', b'Tumblr-square'), (b'fa-long-arrow-down', b'Long-arrow-down'), (b'fa-long-arrow-up', b'Long-arrow-up'), (b'fa-long-arrow-left', b'Long-arrow-left'), (b'fa-long-arrow-right', b'Long-arrow-right'), (b'fa-apple', b'Apple'), (b'fa-windows', b'Windows'), (b'fa-android', b'Android'), (b'fa-linux', b'Linux'), (b'fa-dribbble', b'Dribbble'), (b'fa-skype', b'Skype'), (b'fa-foursquare', b'Foursquare'), (b'fa-trello', b'Trello'), (b'fa-female', b'Female'), (b'fa-male', b'Male'), (b'fa-gittip', b'Gittip'), (b'fa-gratipay', b'Gratipay'), (b'fa-sun-o', b'Sun-o'), (b'fa-moon-o', b'Moon-o'), (b'fa-archive', b'Archive'), (b'fa-bug', b'Bug'), (b'fa-vk', b'Vk'), (b'fa-weibo', b'Weibo'), (b'fa-renren', b'Renren'), (b'fa-pagelines', b'Pagelines'), (b'fa-stack-exchange', b'Stack-exchange'), (b'fa-arrow-circle-o-right', b'Arrow-circle-o-right'), (b'fa-arrow-circle-o-left', b'Arrow-circle-o-left'), (b'fa-toggle-left', b'Toggle-left'), (b'fa-caret-square-o-left', b'Caret-square-o-left'), (b'fa-dot-circle-o', b'Dot-circle-o'), (b'fa-wheelchair', b'Wheelchair'), (b'fa-vimeo-square', b'Vimeo-square'), (b'fa-turkish-lira', b'Turkish-lira'), (b'fa-try', b'Try'), (b'fa-plus-square-o', b'Plus-square-o'), (b'fa-space-shuttle', b'Space-shuttle'), (b'fa-slack', b'Slack'), (b'fa-envelope-square', b'Envelope-square'), (b'fa-wordpress', b'Wordpress'), (b'fa-openid', b'Openid'), (b'fa-institution', b'Institution'), (b'fa-bank', b'Bank'), (b'fa-university', b'University'), (b'fa-mortar-board', b'Mortar-board'), (b'fa-graduation-cap', b'Graduation-cap'), (b'fa-yahoo', b'Yahoo'), (b'fa-google', b'Google'), (b'fa-reddit', b'Reddit'), (b'fa-reddit-square', b'Reddit-square'), (b'fa-stumbleupon-circle', b'Stumbleupon-circle'), (b'fa-stumbleupon', b'Stumbleupon'), (b'fa-delicious', b'Delicious'), (b'fa-digg', b'Digg'), (b'fa-pied-piper', b'Pied-piper'), (b'fa-pied-piper-alt', b'Pied-piper-alt'), (b'fa-drupal', b'Drupal'), (b'fa-joomla', b'Joomla'), (b'fa-language', b'Language'), (b'fa-fax', b'Fax'), (b'fa-building', b'Building'), (b'fa-child', b'Child'), (b'fa-paw', b'Paw'), (b'fa-spoon', b'Spoon'), (b'fa-cube', b'Cube'), (b'fa-cubes', b'Cubes'), (b'fa-behance', b'Behance'), (b'fa-behance-square', b'Behance-square'), (b'fa-steam', b'Steam'), (b'fa-steam-square', b'Steam-square'), (b'fa-recycle', b'Recycle'), (b'fa-automobile', b'Automobile'), (b'fa-car', b'Car'), (b'fa-cab', b'Cab'), (b'fa-taxi', b'Taxi'), (b'fa-tree', b'Tree'), (b'fa-spotify', b'Spotify'), (b'fa-deviantart', b'Deviantart'), (b'fa-soundcloud', b'Soundcloud'), (b'fa-database', b'Database'), (b'fa-file-pdf-o', b'File-pdf-o'), (b'fa-file-word-o', b'File-word-o'), (b'fa-file-excel-o', b'File-excel-o'), (b'fa-file-powerpoint-o', b'File-powerpoint-o'), (b'fa-file-photo-o', b'File-photo-o'), (b'fa-file-picture-o', b'File-picture-o'), (b'fa-file-image-o', b'File-image-o'), (b'fa-file-zip-o', b'File-zip-o'), (b'fa-file-archive-o', b'File-archive-o'), (b'fa-file-sound-o', b'File-sound-o'), (b'fa-file-audio-o', b'File-audio-o'), (b'fa-file-movie-o', b'File-movie-o'), (b'fa-file-video-o', b'File-video-o'), (b'fa-file-code-o', b'File-code-o'), (b'fa-vine', b'Vine'), (b'fa-codepen', b'Codepen'), (b'fa-jsfiddle', b'Jsfiddle'), (b'fa-life-bouy', b'Life-bouy'), (b'fa-life-buoy', b'Life-buoy'), (b'fa-life-saver', b'Life-saver'), (b'fa-support', b'Support'), (b'fa-life-ring', b'Life-ring'), (b'fa-circle-o-notch', b'Circle-o-notch'), (b'fa-ra', b'Ra'), (b'fa-rebel', b'Rebel'), (b'fa-ge', b'Ge'), (b'fa-empire', b'Empire'), (b'fa-git-square', b'Git-square'), (b'fa-git', b'Git'), (b'fa-hacker-news', b'Hacker-news'), (b'fa-tencent-weibo', b'Tencent-weibo'), (b'fa-qq', b'Qq'), (b'fa-wechat', b'Wechat'), (b'fa-weixin', b'Weixin'), (b'fa-send', b'Send'), (b'fa-paper-plane', b'Paper-plane'), (b'fa-send-o', b'Send-o'), (b'fa-paper-plane-o', b'Paper-plane-o'), (b'fa-history', b'History'), (b'fa-genderless', b'Genderless'), (b'fa-circle-thin', b'Circle-thin'), (b'fa-header', b'Header'), (b'fa-paragraph', b'Paragraph'), (b'fa-sliders', b'Sliders'), (b'fa-share-alt', b'Share-alt'), (b'fa-share-alt-square', b'Share-alt-square'), (b'fa-bomb', b'Bomb'), (b'fa-soccer-ball-o', b'Soccer-ball-o'), (b'fa-futbol-o', b'Futbol-o'), (b'fa-tty', b'Tty'), (b'fa-binoculars', b'Binoculars'), (b'fa-plug', b'Plug'), (b'fa-slideshare', b'Slideshare'), (b'fa-twitch', b'Twitch'), (b'fa-yelp', b'Yelp'), (b'fa-newspaper-o', b'Newspaper-o'), (b'fa-wifi', b'Wifi'), (b'fa-calculator', b'Calculator'), (b'fa-paypal', b'Paypal'), (b'fa-google-wallet', b'Google-wallet'), (b'fa-cc-visa', b'Cc-visa'), (b'fa-cc-mastercard', b'Cc-mastercard'), (b'fa-cc-discover', b'Cc-discover'), (b'fa-cc-amex', b'Cc-amex'), (b'fa-cc-paypal', b'Cc-paypal'), (b'fa-cc-stripe', b'Cc-stripe'), (b'fa-bell-slash', b'Bell-slash'), (b'fa-bell-slash-o', b'Bell-slash-o'), (b'fa-trash', b'Trash'), (b'fa-copyright', b'Copyright'), (b'fa-at', b'At'), (b'fa-eyedropper', b'Eyedropper'), (b'fa-paint-brush', b'Paint-brush'), (b'fa-birthday-cake', b'Birthday-cake'), (b'fa-area-chart', b'Area-chart'), (b'fa-pie-chart', b'Pie-chart'), (b'fa-line-chart', b'Line-chart'), (b'fa-lastfm', b'Lastfm'), (b'fa-lastfm-square', b'Lastfm-square'), (b'fa-toggle-off', b'Toggle-off'), (b'fa-toggle-on', b'Toggle-on'), (b'fa-bicycle', b'Bicycle'), (b'fa-bus', b'Bus'), (b'fa-ioxhost', b'Ioxhost'), (b'fa-angellist', b'Angellist'), (b'fa-cc', b'Cc'), (b'fa-shekel', b'Shekel'), (b'fa-sheqel', b'Sheqel'), (b'fa-ils', b'Ils'), (b'fa-meanpath', b'Meanpath'), (b'fa-buysellads', b'Buysellads'), (b'fa-connectdevelop', b'Connectdevelop'), (b'fa-dashcube', b'Dashcube'), (b'fa-forumbee', b'Forumbee'), (b'fa-leanpub', b'Leanpub'), (b'fa-sellsy', b'Sellsy'), (b'fa-shirtsinbulk', b'Shirtsinbulk'), (b'fa-simplybuilt', b'Simplybuilt'), (b'fa-skyatlas', b'Skyatlas'), (b'fa-cart-plus', b'Cart-plus'), (b'fa-cart-arrow-down', b'Cart-arrow-down'), (b'fa-diamond', b'Diamond'), (b'fa-ship', b'Ship'), (b'fa-user-secret', b'User-secret'), (b'fa-motorcycle', b'Motorcycle'), (b'fa-street-view', b'Street-view'), (b'fa-heartbeat', b'Heartbeat'), (b'fa-venus', b'Venus'), (b'fa-mars', b'Mars'), (b'fa-mercury', b'Mercury'), (b'fa-transgender', b'Transgender'), (b'fa-transgender-alt', b'Transgender-alt'), (b'fa-venus-double', b'Venus-double'), (b'fa-mars-double', b'Mars-double'), (b'fa-venus-mars', b'Venus-mars'), (b'fa-mars-stroke', b'Mars-stroke'), (b'fa-mars-stroke-v', b'Mars-stroke-v'), (b'fa-mars-stroke-h', b'Mars-stroke-h'), (b'fa-neuter', b'Neuter'), (b'fa-facebook-official', b'Facebook-official'), (b'fa-pinterest-p', b'Pinterest-p'), (b'fa-whatsapp', b'Whatsapp'), (b'fa-server', b'Server'), (b'fa-user-plus', b'User-plus'), (b'fa-user-times', b'User-times'), (b'fa-hotel', b'Hotel'), (b'fa-bed', b'Bed'), (b'fa-viacoin', b'Viacoin'), (b'fa-train', b'Train'), (b'fa-subway', b'Subway'), (b'fa-medium', b'Medium')]),
        ),
    ]
