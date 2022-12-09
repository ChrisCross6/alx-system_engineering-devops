# kills a process named killmwnow

exec { 'pkill':
  command => 'pkill killmenow'
}
