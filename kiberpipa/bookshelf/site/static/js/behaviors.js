window.jQuery(function ($) {
	$('nav .disabled a, .widget_nav_menu .disabled a').wrapInner('<span></span>').find('span').unwrap();
	
	/* nav select */
	$('.branding nav').each(function () {
		var $w = $(this).addClass('generated'),
			$f = $('<div class="narrow"></div>').prependTo($w),
			$a = $('<a href="#">&mdash;<br />&mdash;<br />&mdash;</a>').prependTo($f),
			$s;
		if (navigator.userAgent.match(/(iPad|iPhone|iPod)/i)) {
			$s = $('<select name="nav" />').appendTo($f).on('change', function () {
				if (this.value) {
					location = this.value;
				}
			});
			// here
			$('<option>-</option>')
				.appendTo($s);
			// home
			$('<option></option>')
				.html($('.branding hgroup h1').html())
				.attr('value', this.href)
				.appendTo($s);
			// nav
			$w.find('li a').each(function () {
				$('<option></option>')
					.html(this.innerHTML)
					.attr('value', this.href)
					.appendTo($s);
			});
			$a.on('click', function (ev) {
				ev.preventDefault();
				$s.trigger('focus');
				$w.scrollTop(0).scrollLeft(0);
			});
		} else {
			$a.on('click', function (ev) {
				ev.preventDefault();
				$w.toggleClass('show');
			})
		}
	});
	
	/* carousel */
	(function () {
		var $e = $('.main .carousel hgroup').css({
				'position': 'relative',
				'width': '100%',
				'top': 0
			}),
			$w = $e.parent();
		function show(dir) {
			var $c = $e.filter(':visible'),
				$n = dir > 0 ? $c.next('hgroup') : $c.prev('hgroup'),
				ac, an, aw;
			if (!$n.length) {
				$n = dir > 0 ? $e.eq(0) : $e.eq(-1);
			}
			$n.removeClass('hidden').css({
				'left': (dir * 100) + '%',
				'top': 0,
				'position': 'absolute',
				'display': 'block',
				'opacity': 0
			});
			ac = $c.animate({'left': (dir * 100 * -1) + '%', 'opacity': 0}, 300, 'linear', function () {
				$c.css('position', 'absolute').hide();
			});
			an = $n.animate({'left': '0%', 'opacity': 1}, 300, 'linear', function () {
				$n.css('position', 'relative');
			});
			aw = $w.animate({'height': $n.outerHeight()}, 300, function () {
				$w.css('height', '');
			});
			return $.when(ac, an, aw);
		}
		function autonext() {
			setTimeout(function () {
				$w.trigger('carouselnext');
			}, 7000);
		}
		if ($e.length > 1) {
			$('<a href="#next" class="flip next">&rsaquo;</a>')
				.appendTo($w)
				.on('click', function (ev) {
					ev.preventDefault();
					$w.off('carouselnext');
					show(1);
				});
			$('<a href="#previous" class="flip previous">&lsaquo;</a>')
				.appendTo($w)
				.on('click', function (ev) {
					ev.preventDefault();
					$w.off('carouselnext');
					show(-1);
				});
			$e.eq(0).css({
				'opacity': 1,
				'left': 0,
				'display': 'block'
			});
			$w.on('carouselnext', function () {
				show(1).done(autonext);
			});
			autonext();
		}
	}());
});