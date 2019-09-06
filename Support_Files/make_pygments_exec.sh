# Install glasgow haskell compiler - ghc, cabal, pandoc in the terminal
sudo apt-get install haskell-platform
sudo cabal install cabal-install pandoc
# All the steps are here :: https://pandoc.org/installing.html

# create the executable like this
# All the steps are here :: https://relentlesscoding.com/2018/08/12/use-pandoc-with-pygments-to-highlight-source-code/
ghc -dynamic pygments.hs
# And infuse the pygments executable like this:
pandoc -F pygments -f markdown -t html5 -o blogpost.html blogpost.md
