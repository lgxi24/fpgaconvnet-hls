#ifndef MEM_READ_TB_HPP_
#define MEM_READ_TB_HPP_

#include "common.hpp"
#include "mem_read_param.hpp"

/////////////////////////////////

void mem_read_top(
    volatile mem_int in_hw[MEM_READ_PORTS_IN][MEM_READ_BATCH_SIZE*MEM_READ_ROWS_IN*MEM_READ_COLS_IN*DIVIDE(MEM_READ_CHANNELS_IN,MEM_READ_STREAMS_IN)],
    stream_t(data_t) in[MEM_READ_STREAMS_IN]
);

/////////////////////////////////

#endif
