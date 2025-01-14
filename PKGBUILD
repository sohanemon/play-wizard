# Maintainer: Sohan Emon <sohanemon@outlook.com>
pkgname=play-wizard
pkgver=1.0.0
pkgrel=1
pkgdesc="Control multiple media players via DBus with a single command."
arch=('any')
url="https://github.com/yourusername/play-wizard"
license=('GPL3')
depends=('python' 'python-dbus')
source=("LICENSE" "Makefile" "play-wizard.py" "README.md")
sha256sums=('SKIP' 'SKIP' 'SKIP' 'SKIP') # Replace with actual checksums if needed

build() {
  echo "No build steps required for this package."
}

package() {
  # Install the script
  install -Dm755 "$srcdir/play-wizard.py" "$pkgdir/usr/bin/play-wizard"

  # Install the Makefile (optional, if used)
  install -Dm644 "$srcdir/Makefile" "$pkgdir/usr/share/play-wizard/Makefile"

  # Install the LICENSE file
  install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # Install the README
  install -Dm644 "$srcdir/README.md" "$pkgdir/usr/share/doc/$pkgname/README.md"
}
