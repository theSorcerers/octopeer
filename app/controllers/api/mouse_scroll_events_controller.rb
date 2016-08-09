class Api::MouseScrollEventsController < ApplicationController
  include TimeHelper
  before_action :set_mouse_scroll_event, only: :show
  before_action only: :create do
    format_time(:mouse_scroll_event)
  end

  def index
    @mouse_scroll_events = MouseScrollEvent.all

    render json: @mouse_scroll_events
  end

  def show
    render json: @mouse_scroll_event
  end

  def create
    @mouse_scroll_event = MouseScrollEvent.new(mouse_scroll_event_params)

    if @mouse_scroll_event.save
      render json: @mouse_scroll_event, status: :created
    else
      render json: @mouse_scroll_event.errors, status: :unprocessable_entity
    end
  end

  private

  def set_mouse_scroll_event
    @mouse_scroll_event = MouseScrollEvent.find(params[:id])
  end

  def mouse_scroll_event_params
    params.require(:mouse_scroll_event).permit(:id, :viewport_x, :viewport_y, :session_id, :created_at)
  end
end
