# Run texcount before each pdflatex invocation to generate the word-count file.
# This avoids the need for -shell-escape entirely.
$pdflatex = 'internal texcount_and_compile %O %S';

sub texcount_and_compile {
    my @args = @_;
    my $src = $args[-1];            # last arg is the source file
    (my $base = $src) =~ s/\.[^.]+$//;  # strip extension
    my $wc_file = "$base.wordcount";

    # texcount -brief prints e.g. "3456+123+..." — capture the first number (body words)
    my $tc_out = `texcount -utf8 -inc -brief "$src" 2>&1`;
    if ($tc_out =~ /^(\d+)/) {
        open my $fh, '>', $wc_file or warn "Cannot write $wc_file: $!";
        print $fh $1;
        close $fh;
    }
    return system('pdflatex', @args);
}
