use clap::Clap;

#[derive(Clap, Debug)]
#[clap(name="gatuby tool")]
struct Opts {
    #[clap(long)]
    title: Option<String>,
    #[clap(long)]
    slug: Option<String>,
    #[clap(long)]
    tags: Option<String>,
    #[clap(long)]
    path: Option<String>,
}

fn main() {
    let opts = Opts::parse();

    let title = match opts.title {
        Some(t) => t,
        _ => String::from(""),
    };

    let slug = match opts.slug {
        Some(s) => s,
        _ => String::from(""),
    };

    let tags = match opts.tags {
        Some(t) => t,
        _ => String::from(""),
    };

    let path = match opts.path {
        Some(p) => p,
        _ => String::from(""),
    };
    println!("{}, {}, {}, {}", title, slug, tags, path);
}
