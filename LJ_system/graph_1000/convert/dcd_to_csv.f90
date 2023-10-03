program main

  use read_dcd
  implicit none

  character(len=50) :: dcd_name, csv_name

  integer :: N, snapshots, snapshot, fnum=302, i, j
  logical :: uc_present
  real, dimension(:,:), allocatable :: positions
  real(kind=real64), dimension(3, 3) :: uc_vecs
  
  CALL GET_COMMAND_ARGUMENT(1, dcd_name)  
  CALL GET_COMMAND_ARGUMENT(2, csv_name)

  
  CALL read_dcd_header(TRIM(dcd_name), N, snapshots, uc_present)

  allocate(positions(3, N))
  open(fnum, file=TRIM(csv_name), status='new')
  
  do snapshot=1, snapshots
     call read_dcd_snapshot(TRIM(dcd_name), N, snapshot, uc_present, positions, uc_vecs)

     write (fnum, "(*(G0,:,','))") uc_vecs
     write (fnum, "(*(G0,:,','))") positions
     write(fnum, *) '\n'
  end do

  deallocate(positions)
  close(fnum)
  
end program main
